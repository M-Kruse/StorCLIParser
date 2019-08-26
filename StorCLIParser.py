#!/usr/bin/env python3
from subprocess import check_output
import os.path

class StorCLIParser:

    def __init__(self):
        self.storcli_bin = '/opt/MegaRAID/storcli/storcli64'
        if not os.path.isfile(self.storcli_bin):
            print("Could not find the storcli bin.")
            print("Please edit self.storcli_bin if it is not in the installed directory")
            exit()

    def ctrl_list(self, storcli_output):
        ctrls = []
        result = storcli_output.split('\nCtl', 1)[1].split("Ctl")[0].split("\n")
        result = [i for i in result if i] 
        for line in result:
            if 'Model' not in line and '---------------' not in line:
                line = line.split()
                line = [i for i in line if i] 
                ctrls.append(line)
        ctrls = [i for i in ctrls if i]
        return ctrls

    def ctrl_info_dict(self, storcli_output):
        ctrl_dict = {}
        for line in storcli_output.split("\n"):
            if ' = ' in line:
                ctrl_dict.update({line.split(" = ")[0].strip(): line.split(" = ")[1].strip()})
        return ctrl_dict

    def pd_list_json(self, storcli_output):
        pds = []
        result = storcli_output.split('\nEID', 1)[1].split('\nEID', 1)[0].split("\n")
        for line in result:
            if '------' not in line and ':Slt' not in line:
                line = line.split(" ")
                line = [i for i in line if i]
                pds.append(line)

        pds = [i for i in pds if i]
        return pds

    def pd_info_dict(self, storcli_output):
        pd_dict = {}
        for line in storcli_output.split("\n"):
            if ' = ' in line:
                pd_dict.update({line.split(" = ")[0].strip(): line.split(" = ")[1].strip()})
        return pd_dict

    def generate_storcli_json(self):
        ctrl_json_template = []
        storcli_show_ctrls = check_output([self.storcli_bin, "show", "all"]).decode("utf-8")
        for ctrl in self.ctrl_list(storcli_show_ctrls):
            ctrl_num = ctrl[0]
            storcli_show_ctrl = check_output([
                                                self.storcli_bin,
                                                "/c{}".format(ctrl_num), "show"]).decode("utf-8")
            ctrl_dict = self.ctrl_info_dict(storcli_show_ctrl)
            virtual_drives_list = []
            for pd in self.pd_list_json(storcli_show_ctrl):
                if pd != {}:
                    pd_list = []
                    enc = pd[0].split(":")[0]
                    slot = pd[0].split(":")[1]
                    storcli_output = check_output([
                                                    self.storcli_bin,
                                                    "/c{}/e{}/s{}".format(ctrl_num, enc, slot),
                                                    "show",
                                                    "all"]).decode("utf-8")
                    pd_dict = self.pd_info_dict(storcli_output)
                    pd_list.append({
                                        'enc': enc,
                                        'slot': slot,
                                        'vendor': pd_dict['Manufacturer Id'],
                                        'serial': pd_dict['SN'],
                                        'model': pd_dict['Model Number'],
                                        'capacity': pd_dict['Raw size'],
                                        'firmware': pd_dict['Firmware Revision'],
                                        'smart_error': pd_dict['S.M.A.R.T alert flagged by drive']})

            ctrl_json_template.append({
                                        'id': ctrl_num,
                                        'model': ctrl_dict['Product Name'],
                                        'serial':ctrl_dict['Serial Number'],
                                        'firmware':ctrl_dict['FW Package Build'],
                                        'virtual_drives': virtual_drives_list,
                                        'pd_list': pd_list})
        final = {}
        final['controllers'] = ctrl_json_template
        return final
