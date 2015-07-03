from collections import OrderedDict

# FEI4A
fei4a = {
    'flavor': 'fei4a',
    'calibration_parameters': OrderedDict([
        ('C_Inj_Low', 2.0),  # fF, C_Low
        ('C_Inj_Med', 4.1),  # fF, C_High
        ('C_Inj_High', 6.05),  # fF, C_Low + C_High
        ('Vcal_Coeff_0', 0.0),  # mV, offset
        ('Vcal_Coeff_1', 1.45),  # mV/PlsrDAC, slope
        ('Pulser_Corr_C_Inj_Low', None),
        ('Pulser_Corr_C_Inj_Med', None),
        ('Pulser_Corr_C_Inj_High', None)
    ]),
    'commands': {
        # fast
        'LV1': {'bitstream': '11101', 'bitlength': 5, 'description': 'Level 1 Trigger: a single bit flip in the LV1 command will still result in a LV1 being decoded'},
        'BCR': {'bitstream': '101100001', 'bitlength': 9, 'description': 'Bunch Counter Reset: the bunch crossing counter is set to zero'},
        'ECR': {'bitstream': '101100010', 'bitlength': 9, 'description': 'Event Counter Reset: clears all memory pointers and data structures without touching configuration memory'},
        'CAL': {'bitstream': '101100100', 'bitlength': 9, 'description': 'Calibration Pulse: digital or analog calibration pulse is distributed to the pixel array'},
        'Slow': {'bitstream': '101101000', 'bitlength': 9, 'description': 'Slow command header'},
        # slow
        'RdRegister': {'bitstream': 'Slow+0001+ChipID+Address', 'bitlength': 23, 'description': 'Read Register: read global memory register'},
        'WrRegister': {'bitstream': 'Slow+0010+ChipID+Address+GlobalData', 'bitlength': 39, 'description': 'Write Register: write global memory register'},
        'WrFrontEnd': {'bitstream': 'Slow+0100+ChipID+000000+PixelData', 'bitlength': 695, 'description': 'Write Pixel: write conf data to selected shift register'},
        'GlobalReset': {'bitstream': 'Slow+1000+ChipID', 'bitlength': 17, 'description': 'Reset Command: puts chip in initial state'},
        'GlobalPulse': {'bitstream': 'Slow+1001+ChipID+Width', 'bitlength': 23, 'description': 'Global Pulse: e.g. functionality determined by the Control Pulser register'},
        'RunMode': {'bitstream': 'Slow+1010+ChipID+111000', 'bitlength': 23, 'description': 'Run Mode'},
        'ConfMode': {'bitstream': 'Slow+1010+ChipID+000111', 'bitlength': 23, 'description': 'Configuration Mode (default for power-up or reset)'},
        # parts
        'ChipID': {'bitlength': 4, 'description': 'Read Register: read global memory register'},
        'Address': {'bitlength': 6, 'description': 'Write Register: write global memory register'},
        'GlobalData': {'bitlength': 16, 'description': 'Gloabal Register data: payload of WrRegister'},
        'PixelData': {'bitlength': 672, 'description': 'Pixel Register data: payload of WrFrontEnd'},
        'Width': {'bitlength': 6, 'description': 'Width of of Global Pulse'},
    },
    'global_registers': {
        'spare_1': {'value': 0, 'address': 1, 'bitlength': 16, 'readonly': True, 'description': ''},
        'spare_2': {'value': 0, 'address': 2, 'bitlength': 11, 'readonly': True, 'description': ''},
        'Conf_AddrEnable': {'value': 1, 'address': 2, 'bitlength': 1, 'offset': 11, 'description': ''},
        'Trig_Count': {'value': 0, 'address': 2, 'bitlength': 4, 'offset': 12, 'description': ''},
        'ErrorMask': {'value': 4292872191, 'address': 3, 'bitlength': 32, 'description': 'ErrorMask[20] is configBit which should stay low by default'},
        'Vthin': {'value': 255, 'address': 5, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'PrmpVbp_R': {'value': 43, 'address': 5, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'PrmpVbp': {'value': 43, 'address': 6, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'DisVbn_CPPM': {'value': 62, 'address': 6, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'DisVbn': {'value': 40, 'address': 7, 'bitlength': 8, 'littleendian': True, 'description': 'Less time walk for higher values. Value from IBL std. tuning.'},
        'TdacVbp': {'value': 240, 'address': 7, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'Amp2VbpFol': {'value': 26, 'address': 8, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'Amp2Vbn': {'value': 79, 'address': 8, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'Amp2Vbp': {'value': 85, 'address': 9, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'PrmpVbp_T': {'value': 0, 'address': 9, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'Amp2Vbpff': {'value': 50, 'address': 10, 'bitlength': 8, 'littleendian': True, 'description': 'FE-I4A manual: Amp2Vbpf, fixes noise on power supply and dead pixels when irradiated'},
        'FdacVbn': {'value': 15, 'address': 10, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'PrmpVbp_L': {'value': 43, 'address': 11, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'PrmpVbnFol': {'value': 106, 'address': 11, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'PrmpVbnLcc': {'value': 0, 'address': 12, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'PrmpVbpf': {'value': 27, 'address': 12, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': 'Std. IBL value. Less it better for TDC measurements.'},
        'spare_13': {'value': 0, 'address': 13, 'bitlength': 1, 'readonly': True, 'description': ''},
        'Pixel_Strobes': {'value': 0, 'address': 13, 'bitlength': 13, 'littleendian': True, 'offset': 1, 'description': 'For SEU hardness set to zero'},
        'S0': {'value': 0, 'address': 13, 'bitlength': 1, 'offset': 14, 'description': ''},
        'S1': {'value': 0, 'address': 13, 'bitlength': 1, 'offset': 15, 'description': ''},
        'BonnDac': {'value': 237, 'address': 14, 'bitlength': 8, 'littleendian': True, 'description': 'littleendian?'},
        'LvdsDrvIref': {'value': 171, 'address': 14, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': 'littleendian?'},
        'LvdsDrvVos': {'value': 105, 'address': 15, 'bitlength': 8, 'littleendian': True, 'description': 'littleendian?'},
        'PllIbias': {'value': 88, 'address': 15, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': ''},
        'PllIcp': {'value': 28, 'address': 16, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'TempSensIbias': {'value': 0, 'address': 16, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': 'littleendian?'},
        'PlsrIdacRamp': {'value': 180, 'address': 17, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'spare_17': {'value': 0, 'address': 17, 'bitlength': 8, 'offset': 8, 'readonly': True, 'description': ''},
        'PlsrVgOpAmp': {'value': 255, 'address': 18, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'spare_18': {'value': 0, 'address': 18, 'bitlength': 8, 'offset': 8, 'readonly': True, 'description': ''},
        'spare_19': {'value': 0, 'address': 19, 'bitlength': 8, 'readonly': True, 'description': ''},
        'PlsrDacBias': {'value': 96, 'address': 19, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': ''},
        'Vthin_AltFine': {'value': 80, 'address': 20, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'Vthin_AltCoarse': {'value': 0, 'address': 20, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': ''},
        'PlsrDAC': {'value': 0, 'address': 21, 'bitlength': 10, 'littleendian': True, 'description': ''},
        'DIGHITIN_SEL': {'value': 0, 'address': 21, 'bitlength': 1, 'offset': 10, 'description': ''},
        'DINJ_OVERRIDE': {'value': 0, 'address': 21, 'bitlength': 1, 'offset': 11, 'description': ''},
        'HITLD_IN': {'value': 0, 'address': 21, 'bitlength': 1, 'offset': 12, 'description': ''},
        'spare_21': {'value': 0, 'address': 21, 'bitlength': 3, 'offset': 13, 'readonly': True, 'description': ''},
        'spare_22_0': {'value': 0, 'address': 22, 'bitlength': 2, 'readonly': True, 'description': ''},
        'Colpr_Addr': {'value': 0, 'address': 22, 'bitlength': 6, 'offset': 2, 'littleendian': True, 'description': ''},
        'Colpr_Mode': {'value': 0, 'address': 22, 'bitlength': 2, 'offset': 8, 'littleendian': True, 'description': ''},
        'spare_22_1': {'value': 0, 'address': 22, 'bitlength': 6, 'offset': 10, 'readonly': True, 'description': ''},
        'DisableColumnCnfg': {'value': 0, 'address': 23, 'bitlength': 40, 'littleendian': True, 'description': 'Disables digital double columns'},
        'Trig_Lat': {'value': 210, 'address': 25, 'bitlength': 8, 'offset': 8, 'description': ''},
        'HitDiscCnfg': {'value': 0, 'address': 26, 'bitlength': 2, 'description': ''},
        'StopModeCnfg': {'value': 0, 'address': 26, 'bitlength': 1, 'offset': 2, 'description': ''},
        'CMDcnt': {'value': 11, 'address': 26, 'bitlength': 14, 'offset': 3, 'description': ''},
        'SR_Clock': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 1, 'description': 'aka FE_clk_pulse'},
        'Latch_En': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 2, 'description': ''},
        'SR_Clr': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 3, 'description': ''},
        'CalEn': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 4, 'description': ''},
        'GateHitOr': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 5, 'description': 'Enables FEI4 self-trigger'},
        'spare_27': {'value': 0, 'address': 27, 'bitlength': 5, 'offset': 6, 'readonly': True, 'description': ''},
        'ReadSkipped': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 11, 'description': ''},
        'ReadErrorReq': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 12, 'description': ''},
        'StopClkPulse': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 13, 'description': ''},
        'Efuse_Sense': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 14, 'description': ''},
        'EN_PLL': {'value': 1, 'address': 27, 'bitlength': 1, 'offset': 15, 'description': ''},
        'EN_320M': {'value': 0, 'address': 28, 'bitlength': 1, 'description': ''},
        'EN_160M': {'value': 1, 'address': 28, 'bitlength': 1, 'offset': 1, 'description': ''},
        'CLK0_S2': {'value': 1, 'address': 28, 'bitlength': 1, 'offset': 2, 'description': ''},
        'CLK0_S1': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 3, 'description': ''},
        'CLK0_S0': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 4, 'description': ''},
        'CLK1_S2': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 5, 'description': ''},
        'CLK1_S1': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 6, 'description': ''},
        'CLK1_S0': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 7, 'description': ''},
        'EN_80M': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 8, 'description': ''},
        'EN_40M': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 9, 'description': ''},
        'spare_28': {'value': 0, 'address': 28, 'bitlength': 5, 'offset': 10, 'readonly': True, 'description': ''},
        'LvdsDrvSet06': {'value': 1, 'address': 28, 'bitlength': 1, 'offset': 15, 'description': ''},
        'LvdsDrvSet12': {'value': 1, 'address': 29, 'bitlength': 1, 'offset': 0, 'description': ''},
        'LvdsDrvSet30': {'value': 1, 'address': 29, 'bitlength': 1, 'offset': 1, 'description': ''},
        'LvdsDrvEn': {'value': 1, 'address': 29, 'bitlength': 1, 'offset': 2, 'description': ''},
        'spare_29_0': {'value': 0, 'address': 29, 'bitlength': 1, 'offset': 3, 'readonly': True, 'description': ''},
        'EmptyRecordCnfg': {'value': 0, 'address': 29, 'bitlength': 8, 'offset': 4, 'description': ''},
        'Clk2OutCnfg': {'value': 0, 'address': 29, 'bitlength': 1, 'offset': 12, 'description': ''},
        'No8b10b': {'value': 0, 'address': 29, 'bitlength': 1, 'offset': 13, 'description': ''},
        'spare_29_1': {'value': 0, 'address': 29, 'bitlength': 2, 'offset': 14, 'readonly': True, 'description': ''},
        'spare_30': {'value': 0, 'address': 30, 'bitlength': 16, 'readonly': True, 'description': ''},
        'spare_31': {'value': 0, 'address': 31, 'bitlength': 4, 'readonly': True, 'description': ''},
        'ExtAnaCalSW': {'value': 0, 'address': 31, 'bitlength': 1, 'offset': 4, 'description': ''},
        'ExtDigCalSW': {'value': 0, 'address': 31, 'bitlength': 1, 'offset': 5, 'description': ''},
        'PlsrDelay': {'value': 2, 'address': 31, 'bitlength': 6, 'offset': 6, 'littleendian': True, 'description': ''},
        'PlsrPwr': {'value': 1, 'address': 31, 'bitlength': 1, 'offset': 12, 'description': ''},
        'PlsrRiseUpTau': {'value': 7, 'address': 31, 'bitlength': 3, 'offset': 13, 'description': 'bigendian?'},
        'SELB': {'value': 0, 'address': 32, 'bitlength': 40, 'register_littleendian': True, 'description': ''},
        'spare_34': {'value': 0, 'address': 34, 'bitlength': 4, 'offset': 8, 'readonly': True, 'register_littleendian': True, 'description': ''},
        'Cref': {'value': 13, 'address': 34, 'bitlength': 4, 'offset': 12, 'littleendian': True, 'register_littleendian': True, 'description': ''},
        'Chip_SN': {'value': 0, 'address': 35, 'bitlength': 16, 'description': ''},
        '0_64': {'value': 0, 'address': 36, 'bitlength': 64, 'readonly': True, 'description': ''},
        '0010101010101010': {'value': 10922, 'address': 40, 'bitlength': 16, 'readonly': True, 'value': 10922, 'description': ''},
        '10101010': {'value': 170, 'address': 41, 'bitlength': 8, 'readonly': True, 'value': 170, 'description': ''},
        'EOCHLSkipped': {'value': 0, 'address': 41, 'bitlength': 8, 'offset': 8, 'readonly': True, 'description': ''},
        'CMDErrReg': {'value': 0, 'address': 42, 'bitlength': 16, 'readonly': True, 'description': ''},
        '0_336': {'value': 0, 'address': 43, 'bitlength': 336, 'readonly': True, 'description': ''}
    },
    'pixel_registers': {
        'Enable': {'value': 1, 'bitlength': 1, 'pxstrobe': 0, 'description': 'Enabling/disabling readout'},
        'TDAC': {'value': 16, 'bitlength': 5, 'pxstrobe': 1, 'littleendian': True, 'description': 'The higher the value, the lower the threshold. Step size can be adjusted by TdacVbp'},
        'C_High': {'value': 1, 'bitlength': 1, 'pxstrobe': 6, 'description': 'Big injection capacitor (nominally 3.8fF/ measured 4.1fF)'},
        'C_Low': {'value': 1, 'bitlength': 1, 'pxstrobe': 7, 'description': 'Big injection capacitor (nominally 1.9fF/ measured 2fF)'},
        'Imon': {'value': 1, 'bitlength': 1, 'pxstrobe': 8, 'description': 'Disabling Imon enables hit-OR'},
        'FDAC': {'value': 8, 'bitlength': 4, 'pxstrobe': 9, 'description': 'The higher the value, the higher the feedback current. Step size can be adjusted by FdacVbn'},
        'EnableDigInj': {'value': 0, 'bitlength': 1, 'pxstrobe': 'SR', 'description': 'SR is non-existing pixel register'}
    }
}

# FEI4B
d = dict(fei4a)
d.update({
    'flavor': 'fei4b',
    'global_registers': {
        'spare_0': {'value': 0, 'address': 0, 'bitlength': 16, 'readonly': True, 'description': ''},
        'EventLimit': {'value': 0, 'address': 1, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'SmallHitErase': {'value': 0, 'address': 1, 'bitlength': 1, 'offset': 8, 'description': ''},
        'spare_1': {'value': 0, 'address': 1, 'bitlength': 7, 'offset': 9, 'readonly': True, 'description': ''},
        'spare_2': {'value': 0, 'address': 2, 'bitlength': 11, 'readonly': True, 'description': ''},
        'Conf_AddrEnable': {'value': 1, 'address': 2, 'bitlength': 1, 'offset': 11, 'description': ''},
        'Trig_Count': {'value': 0, 'address': 2, 'bitlength': 4, 'offset': 12, 'description': ''},
        'ErrorMask': {'value': 4292986879, 'address': 3, 'bitlength': 32, 'description': ''},
        'GADCVref': {'value': 160, 'address': 5, 'bitlength': 8, 'littleendian': True, 'description': 'also BufVgOpAmp, 160 from IBL tuning'},
        'PrmpVbp_R': {'value': 43, 'address': 5, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'PrmpVbp': {'value': 43, 'address': 6, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'spare_6': {'value': 0, 'address': 6, 'bitlength': 8, 'offset': 8, 'readonly': True, 'description': ''},
        'DisVbn': {'value': 40, 'address': 7, 'bitlength': 8, 'littleendian': True, 'description': 'Less time walk for higher values. Value from IBL std. tuning.'},
        'TdacVbp': {'value': 100, 'address': 7, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'Amp2VbpFol': {'value': 26, 'address': 8, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'Amp2Vbn': {'value': 79, 'address': 8, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'Amp2Vbp': {'value': 85, 'address': 9, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'spare_9': {'value': 0, 'address': 9, 'bitlength': 8, 'offset': 8, 'readonly': True, 'description': ''},
        'Amp2Vbpff': {'value': 50, 'address': 10, 'bitlength': 8, 'littleendian': True, 'description': 'FE-I4A manual: Amp2Vbpf, fixes noise on power supply and dead pixels when irradiated'},
        'FdacVbn': {'value': 30, 'address': 10, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'PrmpVbp_L': {'value': 43, 'address': 11, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'PrmpVbnFol': {'value': 106, 'address': 11, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': ''},
        'PrmpVbnLcc': {'value': 0, 'address': 12, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'PrmpVbpf': {'value': 27, 'address': 12, 'bitlength': 8, 'littleendian': True, 'offset': 8, 'description': 'Std. IBL value. Less it better for TDC measurements.'},
        'spare_13': {'value': 0, 'address': 13, 'bitlength': 1, 'readonly': True, 'description': ''},
        'Pixel_Strobes': {'value': 0, 'address': 13, 'bitlength': 13, 'littleendian': True, 'offset': 1, 'description': 'For SEU hardness set to zero'},
        'S0': {'value': 0, 'address': 13, 'bitlength': 1, 'offset': 14, 'description': ''},
        'S1': {'value': 0, 'address': 13, 'bitlength': 1, 'offset': 15, 'description': ''},
        'GADCCompBias': {'value': 100, 'address': 14, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'LVDSDrvIref': {'value': 171, 'address': 14, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': ''},
        'LvdsDrvVos': {'value': 105, 'address': 15, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'PllIbias': {'value': 88, 'address': 15, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': ''},
        'PllIcp': {'value': 28, 'address': 16, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'TempSensIbias': {'value': 0, 'address': 16, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': ''},
        'PlsrIdacRamp': {'value': 180, 'address': 17, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'spare_17': {'value': 0, 'address': 17, 'bitlength': 8, 'offset': 8, 'readonly': True, 'description': ''},
        'PlsrVgOpAmp': {'value': 255, 'address': 18, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'VrefDigTune': {'value': 100, 'address': 18, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': 'digital voltage (1.2V)'},
        'VrefAnTune': {'value': 0, 'address': 19, 'bitlength': 8, 'littleendian': True, 'description': '0 is max. analog voltage (approx. 1.45V)'},
        'PlsrDacBias': {'value': 96, 'address': 19, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': ''},
        'Vthin_AltFine': {'value': 80, 'address': 20, 'bitlength': 8, 'littleendian': True, 'description': ''},
        'Vthin_AltCoarse': {'value': 0, 'address': 20, 'bitlength': 8, 'offset': 8, 'littleendian': True, 'description': ''},
        'PlsrDAC': {'value': 0, 'address': 21, 'bitlength': 10, 'littleendian': True, 'description': ''},
        'DIGHITIN_SEL': {'value': 0, 'address': 21, 'bitlength': 1, 'offset': 10, 'description': ''},
        'DINJ_OVERRIDE': {'value': 0, 'address': 21, 'bitlength': 1, 'offset': 11, 'description': ''},
        'HITLD_IN': {'value': 0, 'address': 21, 'bitlength': 1, 'offset': 12, 'description': ''},
        'spare_21': {'value': 0, 'address': 21, 'bitlength': 3, 'offset': 13, 'readonly': True, 'description': ''},
        'spare_22_0': {'value': 0, 'address': 22, 'bitlength': 2, 'readonly': True, 'description': ''},
        'Colpr_Addr': {'value': 0, 'address': 22, 'bitlength': 6, 'offset': 2, 'littleendian': True, 'description': ''},
        'Colpr_Mode': {'value': 0, 'address': 22, 'bitlength': 2, 'offset': 8, 'littleendian': True, 'description': ''},
        'spare_22_1': {'value': 0, 'address': 22, 'bitlength': 6, 'offset': 10, 'readonly': True, 'description': ''},
        'DisableColumnCnfg': {'value': 0, 'address': 23, 'bitlength': 40, 'littleendian': True, 'description': 'Disables digital double columns'},
        'Trig_Lat': {'value': 210, 'address': 25, 'bitlength': 8, 'offset': 8, 'description': ''},
        'HitDiscCnfg': {'value': 0, 'address': 26, 'bitlength': 2, 'description': ''},
        'StopModeCnfg': {'value': 0, 'address': 26, 'bitlength': 1, 'offset': 2, 'description': ''},
        'CMDcnt': {'value': 11, 'address': 26, 'bitlength': 14, 'offset': 3, 'description': ''},
        'SR_Clock': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 1, 'description': 'aka FE_clk_pulse'},
        'Latch_En': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 2, 'description': ''},
        'SR_Clr': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 3, 'description': ''},
        'CalEn': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 4, 'description': ''},
        'GateHitOr': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 5, 'description': 'Enables FEI4 self-trigger'},
        'spare_27_0': {'value': 0, 'address': 27, 'bitlength': 3, 'offset': 6, 'readonly': True, 'description': ''},
        'SR_Read': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 9, 'description': 'This bit must be pulsed to set up the end of chip logic to receive and pack pixel shift register bits into data records for output. Set bit high before each WriteFrontEnd command'},
        'GADCStart': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 10, 'description': 'also GADCEn'},
        'spare_27_1': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 11, 'readonly': True, 'description': ''},
        'ReadErrorReq': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 12, 'description': ''},
        'StopClkPulse': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 13, 'description': ''},
        'Efuse_Sense': {'value': 0, 'address': 27, 'bitlength': 1, 'offset': 14, 'description': ''},
        'EN_PLL': {'value': 1, 'address': 27, 'bitlength': 1, 'offset': 15, 'description': ''},
        'EN_320M': {'value': 0, 'address': 28, 'bitlength': 1, 'description': ''},
        'EN_160M': {'value': 1, 'address': 28, 'bitlength': 1, 'offset': 1, 'description': ''},
        'CLK0_S2': {'value': 1, 'address': 28, 'bitlength': 1, 'offset': 2, 'description': ''},
        'CLK0_S1': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 3, 'description': ''},
        'CLK0_S0': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 4, 'description': ''},
        'CLK1_S2': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 5, 'description': ''},
        'CLK1_S1': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 6, 'description': ''},
        'CLK1_S0': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 7, 'description': ''},
        'EN_80M': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 8, 'description': ''},
        'EN_40M': {'value': 0, 'address': 28, 'bitlength': 1, 'offset': 9, 'description': ''},
        'spare_28': {'value': 0, 'address': 28, 'bitlength': 5, 'offset': 10, 'readonly': True, 'description': ''},
        'LvdsDrvSet06': {'value': 1, 'address': 28, 'bitlength': 1, 'offset': 15, 'description': ''},
        'LvdsDrvSet12': {'value': 1, 'address': 29, 'bitlength': 1, 'offset': 0, 'description': ''},
        'LvdsDrvSet30': {'value': 1, 'address': 29, 'bitlength': 1, 'offset': 1, 'description': ''},
        'LvdsDrvEn': {'value': 1, 'address': 29, 'bitlength': 1, 'offset': 2, 'description': ''},
        'spare_29_0': {'value': 0, 'address': 29, 'bitlength': 1, 'offset': 3, 'readonly': True, 'description': ''},
        'EmptyRecordCnfg': {'value': 0, 'address': 29, 'bitlength': 8, 'offset': 4, 'description': ''},
        'Clk2OutCnfg': {'value': 0, 'address': 29, 'bitlength': 1, 'offset': 12, 'description': ''},
        'No8b10b': {'value': 0, 'address': 29, 'bitlength': 1, 'offset': 13, 'description': ''},
        'spare_29_1': {'value': 0, 'address': 29, 'bitlength': 2, 'offset': 14, 'readonly': True, 'description': ''},
        'spare_30': {'value': 0, 'address': 30, 'bitlength': 12, 'readonly': True, 'description': ''},
        'MonleakRange': {'value': 0, 'address': 30, 'bitlength': 1, 'offset': 12, 'description': ''},
        'TempSensDisable': {'value': 1, 'address': 30, 'bitlength': 1, 'offset': 13, 'description': ''},
        'TempSensDiodeBiasSel': {'value': 0, 'address': 30, 'bitlength': 2, 'offset': 14, 'littleendian': True, 'description': ''},
        'GADCSel': {'value': 0, 'address': 31, 'bitlength': 3, 'description': ''},
        'spare_31': {'value': 0, 'address': 31, 'bitlength': 1, 'offset': 3, 'readonly': True, 'description': ''},
        'ExtAnaCalSW': {'value': 0, 'address': 31, 'bitlength': 1, 'offset': 4, 'description': ''},
        'ExtDigCalSW': {'value': 0, 'address': 31, 'bitlength': 1, 'offset': 5, 'description': ''},
        'PlsrDelay': {'value': 2, 'address': 31, 'bitlength': 6, 'offset': 6, 'littleendian': True, 'description': ''},
        'PlsrPwr': {'value': 1, 'address': 31, 'bitlength': 1, 'offset': 12, 'description': ''},
        'PlsrRiseUpTau': {'value': 7, 'address': 31, 'bitlength': 3, 'offset': 13, 'description': 'bigendian'},
        'SELB': {'value': 0, 'address': 32, 'bitlength': 40, 'register_littleendian': True, 'description': ''},
        'spare_34_0': {'value': 0, 'address': 34, 'bitlength': 3, 'offset': 8, 'readonly': True, 'register_littleendian': True, 'description': ''},
        'PrmpVbpMsbEn': {'value': 0, 'address': 34, 'bitlength': 1, 'offset': 11, 'register_littleendian': True, 'description': 'Enables bit 7 of PrmpVbp'},
        'spare_34_1': {'value': 0, 'address': 34, 'bitlength': 4, 'offset': 12, 'readonly': True, 'register_littleendian': True, 'description': ''},
        'Chip_SN': {'value': 0, 'address': 35, 'bitlength': 16, 'description': ''},
        '0_64': {'value': 0, 'address': 36, 'bitlength': 64, 'readonly': True, 'description': ''},
        'GADCSelRB': {'value': 0, 'address': 40, 'bitlength': 3, 'readonly': True, 'littleendian': True, 'description': ''},
        'GADCStatus': {'value': 0, 'address': 40, 'bitlength': 1, 'offset': 3, 'readonly': True, 'description': ''},
        'GADCout': {'value': 0, 'address': 40, 'bitlength': 10, 'offset': 4, 'readonly': True, 'description': ''},
        '00': {'value': 0, 'address': 40, 'bitlength': 2, 'offset': 14, 'readonly': True, 'description': ''},
        '10101010': {'value': 170, 'address': 41, 'bitlength': 8, 'readonly': True, 'value': 170, 'description': ''},
        'EOCHLSkipped': {'value': 0, 'address': 41, 'bitlength': 8, 'offset': 8, 'readonly': True, 'description': 'FE-I4B manual: EventLimit'},
        'CMDErrReg': {'value': 0, 'address': 42, 'bitlength': 16, 'readonly': True, 'description': ''},
        '0_336': {'value': 0, 'address': 43, 'bitlength': 336, 'readonly': True, 'description': ''}
    }
})
fei4b = d
