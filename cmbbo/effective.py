#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import math
import json
import sys

popu1 = {'elite_migration_time': 0.0, 'power_cost': [4067.3957759999994, 3615.4629119999995, 4971.261504], 'c_rp': [0.3476773696792811, 0.11455005866756107, 0.05884411964737235, 0.10165427086229983, 0.2199332607717443, 0.08289166375232593, 0.4412437461559323, 0.10625430018428228, 0.41120267284675616, 0.4446576335489399, 0.08916556185315327, 0.23188908760138988, 0.2837471434016384, 0.24498518752893944, 0.1977057920016162], 'h_balance_cost': [1959591.3048185562, 1995550.1078907368, 1768866.1130818492], 'v_rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'elite_h_balance': 1959591.3048185562, 'v_balance_cost': [3.5725401343598304, 1.7610203432347022, 4.133625919613498], 'elite_power': 4067.3957759999994, 'v_p_cost': [[0, 0, 0.4446576335489399, 0.24498518752893944, 0.4412437461559323, 0, 0, 0, 0.27877738041911665, 0, 0.6858207574649533, 0.08916556185315327, 0.18454593461462576, 0.6949498162483946, 0.31225585066917727], [0, 0.05884411964737235, 0.5676106304510253, 0.10625430018428228, 0.4412437461559323, 0.6561878603756957, 0, 0.4446576335489399, 0, 0, 0.40142141252233055, 0.38540141426393826, 0, 0, 0.3147807513537158], [0, 0.8166862508853678, 0.2199332607717443, 0, 0.4446576335489399, 0, 0, 0, 0.10625430018428228, 0.11455005866756107, 0.08916556185315327, 0.23188908760138988, 0.1977057920016162, 0.8718127795875393, 0.2837471434016384]], 'rank': [3, 3, 6], 'h_p_cost': [[1.0, 0, 1.0, 1.0, 0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 0, 0, 1.0, 0], [1.0, 0, 1.0, 1.0, 0, 0, 1.0, 1.0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0], [0, 1.0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 0]], 'h_m_cost': [[1.0, 0, 1.0, 1.0, 0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 0, 0, 1.0, 0], [1.0, 0, 1.0, 1.0, 0, 0, 1.0, 1.0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0], [0, 1.0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 0]], 'v_m_cost': [[0, 0, 0.3729955569579614, 0.05871593730201771, 0.2526554923321813, 0, 0, 0, 0.059812889614661524, 0, 0.7006794901080834, 0.11341557219910925, 0.10745259847555866, 0.747210226283022, 0.33633311480588324], [0, 0.04979595715943638, 0.5025794637836059, 0.1518741038518876, 0.2526554923321813, 0.4566788145065813, 0, 0.3729955569579614, 0, 0, 0.4497486870049925, 0.3960152223746704, 0, 0, 0.11692758010716173], [0, 0.5532426449622297, 0.010016932455225142, 0, 0.3729955569579614, 0, 0, 0, 0.1518741038518876, 0.21537288855332354, 0.11341557219910925, 0.056242854927815084, 0.1209602262525597, 0.8059027488399086, 0.3492473490784584]], 'migration_time': [0.0, 0.0, 0.0], 'c_rm': [0.4925625313283807, 0.21537288855332354, 0.04979595715943638, 0.046767873296212015, 0.010016932455225142, 0.060684725179346644, 0.2526554923321813, 0.1518741038518876, 0.39796287720456364, 0.3729955569579614, 0.11341557219910925, 0.056242854927815084, 0.3492473490784584, 0.05871593730201771, 0.1209602262525597], 'elite_v_balance': 3.5725401343598304, 'v_rp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'init_save': [[[10, 7], [14, 3], [8, 13], [12, 0], [8, 13], [12, 0], [4, 9], [10, 7], [13, 10], [2, 5], [11, 8], [10, 7], [13, 10], [3, 2], [14, 3]], [[2, 3], [10, 12], [2, 3], [11, 11], [11, 11], [10, 12], [4, 2], [3, 14], [5, 6], [7, 13], [10, 12], [2, 3], [12, 10], [5, 6], [10, 12]], [[2, 11], [11, 13], [1, 5], [14, 2], [2, 11], [13, 12], [9, 1], [8, 6], [12, 8], [4, 7], [10, 10], [12, 8], [3, 14], [2, 11], [12, 8]]], 'elite_chrom': [[10, 7], [14, 3], [8, 13], [12, 0], [8, 13], [12, 0], [4, 9], [10, 7], [13, 10], [2, 5], [11, 8], [10, 7], [13, 10], [3, 2], [14, 3]], 'population': [[[10, 7], [14, 3], [8, 13], [12, 0], [8, 13], [12, 0], [4, 9], [10, 7], [13, 10], [2, 5], [11, 8], [10, 7], [13, 10], [3, 2], [14, 3]], [[2, 3], [10, 12], [1, 0], [11, 11], [2, 3], [14, 7], [4, 2], [3, 14], [5, 6], [7, 13], [10, 12], [14, 1], [11, 11], [5, 6], [10, 12]], [[13, 12], [9, 1], [1, 5], [1, 5], [2, 11], [13, 12], [13, 12], [8, 6], [1, 5], [4, 7], [10, 10], [11, 13], [14, 2], [1, 5], [12, 8]]]}
popu2 = {'elite_migration_time': 0.0, 'power_cost': [4067.3957759999994, 5423.194368, 4519.32864], 'c_rp': [0.3410700564072743, 0.21748923465827436, 0.13401067073880568, 0.12117990079827201, 0.09905372934286866, 0.399138402839343, 0.3762046924367879, 0.35604258422437174, 0.476230565680264, 0.48596186036657335, 0.13593326822417862, 0.4354215231398624, 0.010535027391806395, 0.44172080174464634, 0.1332628596497094], 'h_balance_cost': [1959591.3048185562, 1599999.6004000527, 1885617.6122310727], 'v_rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'elite_h_balance': 1959591.3048185562, 'v_balance_cost': [0.9102447757844481, 0.8406966239418061, 0.9456538140325712], 'elite_power': 4067.3957759999994, 'v_p_cost': [[0, 0, 0, 0, 0.476230565680264, 0, 0.399138402839343, 0.48596186036657335, 0.1332628596497094, 0, 0.4354215231398624, 0.21748923465827436, 0.35604258422437174, 0.3410700564072743, 0.13401067073880568], [0.21748923465827436, 0.3410700564072743, 0.4354215231398624, 0, 0.13593326822417862, 0, 0.12117990079827201, 0.1332628596497094, 0, 0, 0.13401067073880568, 0, 0.09905372934286866, 0.48596186036657335, 0.399138402839343], [0.48596186036657335, 0.21748923465827436, 0, 0.476230565680264, 0.010535027391806395, 0, 0, 0, 0, 0.35604258422437174, 0.12117990079827201, 0, 0.44172080174464634, 0.3410700564072743, 0.13401067073880568]], 'rank': [3, 3, 6], 'h_p_cost': [[1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0, 0], [1.0, 0, 0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 0, 1.0, 1.0], [0, 1.0, 1.0, 1.0, 0, 0, 1.0, 1.0, 0, 1.0, 1.0, 0, 1.0, 0, 1.0]], 'h_m_cost': [[1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0, 0], [1.0, 0, 0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 0, 1.0, 1.0], [0, 1.0, 1.0, 1.0, 0, 0, 1.0, 1.0, 0, 1.0, 1.0, 0, 1.0, 0, 1.0]], 'v_m_cost': [[0, 0, 0, 0, 0.4462678715142516, 0, 0.29137492555411665, 0.4236552673771511, 0.06399632520294021, 0, 0.3683472377469954, 0.046886086570668256, 0.36024943005723925, 0.4713670513943852, 0.2464661372660051], [0.046886086570668256, 0.4713670513943852, 0.3683472377469954, 0, 0.2301045982344767, 0, 0.15436665258859153, 0.06399632520294021, 0, 0, 0.2464661372660051, 0, 0.21895531141915806, 0.4236552673771511, 0.29137492555411665], [0.4236552673771511, 0.046886086570668256, 0, 0.4462678715142516, 0.008602627380294409, 0, 0, 0, 0, 0.36024943005723925, 0.15436665258859153, 0, 0.4500623297103077, 0.4713670513943852, 0.2464661372660051]], 'migration_time': [0.0, 0.0, 0.0], 'c_rm': [0.4713670513943852, 0.046886086570668256, 0.2464661372660051, 0.15436665258859153, 0.21895531141915806, 0.29137492555411665, 0.4947792974216388, 0.36024943005723925, 0.4462678715142516, 0.4236552673771511, 0.2301045982344767, 0.3683472377469954, 0.008602627380294409, 0.4500623297103077, 0.06399632520294021], 'elite_v_balance': 0.9102447757844481, 'v_rp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'init_save': [[[13, 10], [11, 4], [14, 5], [11, 4], [14, 5], [6, 11], [6, 11], [12, 0], [4, 6], [7, 12], [12, 0], [10, 3], [10, 3], [11, 4], [8, 9]], [[1, 13], [4, 3], [10, 4], [6, 6], [12, 7], [14, 14], [11, 12], [0, 11], [14, 14], [8, 9], [4, 3], [2, 0], [3, 2], [2, 0], [7, 10]], [[13, 7], [1, 6], [14, 3], [10, 9], [14, 3], [14, 3], [4, 2], [0, 10], [3, 14], [0, 10], [14, 3], [6, 5], [12, 12], [2, 8], [4, 2]]], 'elite_chrom': [[13, 10], [11, 4], [14, 5], [11, 4], [14, 5], [6, 11], [6, 11], [12, 0], [4, 6], [7, 12], [12, 0], [10, 3], [10, 3], [11, 4], [8, 9]], 'population': [[[13, 10], [11, 4], [14, 5], [11, 4], [14, 5], [6, 11], [6, 11], [12, 0], [4, 6], [7, 12], [12, 0], [10, 3], [10, 3], [11, 4], [8, 9]], [[1, 13], [0, 11], [10, 4], [6, 6], [12, 7], [14, 14], [14, 14], [0, 11], [14, 14], [13, 8], [4, 3], [2, 0], [0, 11], [12, 7], [7, 10]], [[13, 7], [1, 6], [14, 3], [10, 9], [14, 3], [14, 3], [14, 3], [9, 1], [3, 14], [0, 10], [0, 10], [3, 14], [4, 2], [12, 12], [4, 2]]]}
popu3 = {'elite_migration_time': 0.0, 'power_cost': [5423.194368, 4971.261504, 3615.4629119999995], 'c_rp': [0.2388595642073536, 0.02302616006879593, 0.3806149112887331, 0.049260389349678524, 0.4543893932709631, 0.2817394258746713, 0.4271038577723465, 0.4933018734816839, 0.19953153320081884, 0.26531558362191715, 0.3096087768354556, 0.2591429619444387, 0.13297902286547358, 0.19596032030816463, 0.449067773608077], 'h_balance_cost': [1599999.6004000527, 1768866.1130818494, 1995550.107890737], 'v_rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'elite_h_balance': 1768866.1130818494, 'v_balance_cost': [0.8111424311378898, 0.7579989333740315, 0.7931557985548794], 'elite_power': 4971.261504, 'v_p_cost': [[0.13297902286547358, 0.4271038577723465, 0.26531558362191715, 0.449067773608077, 0.4543893932709631, 0.19953153320081884, 0.049260389349678524, 0.2591429619444387, 0.3806149112887331, 0, 0, 0.02302616006879593, 0.4933018734816839, 0.2388595642073536, 0], [0.049260389349678524, 0.02302616006879593, 0.2817394258746713, 0, 0.4933018734816839, 0, 0.4271038577723465, 0, 0, 0.2388595642073536, 0.3806149112887331, 0, 0, 0, 0], [0, 0, 0.19596032030816463, 0.02302616006879593, 0.26531558362191715, 0.2388595642073536, 0.4271038577723465, 0, 0, 0.13297902286547358, 0.19953153320081884, 0, 0, 0.3806149112887331, 0.4933018734816839]], 'rank': [4, 3, 5], 'h_p_cost': [[0, 1.0, 0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0, 0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 0, 1.0, 1.0, 0, 0, 0, 0], [1.0, 0, 0, 1.0, 0, 1.0, 1.0, 1.0, 0, 0, 2.0, 1.0, 0, 1.0, 0]], 'h_m_cost': [[0, 1.0, 0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0, 0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 0, 1.0, 1.0, 0, 0, 0, 0], [1.0, 0, 0, 1.0, 0, 1.0, 1.0, 1.0, 0, 0, 2.0, 1.0, 0, 1.0, 0]], 'v_m_cost': [[0.02155704840381803, 0.38039854499156894, 0.48019735064000013, 0.3081417932949942, 0.2706513449987049, 0.2304931996296035, 0.04050079773256576, 0.4131013610088409, 0.35157035195220426, 0, 0, 0.01951371019774331, 0.4353347254441928, 0.09499073632690469, 0], [0.04050079773256576, 0.01951371019774331, 0.2504668692702069, 0, 0.4353347254441928, 0, 0.38039854499156894, 0, 0, 0.09499073632690469, 0.35157035195220426, 0, 0, 0, 0], [0, 0, 0.07652398270897848, 0.01951371019774331, 0.48019735064000013, 0.09499073632690469, 0.38039854499156894, 0, 0, 0.02155704840381803, 0.2304931996296035, 0, 0, 0.35157035195220426, 0.4353347254441928]], 'migration_time': [0.0, 0.0, 0.0], 'c_rm': [0.09499073632690469, 0.01951371019774331, 0.35157035195220426, 0.04050079773256576, 0.2706513449987049, 0.2504668692702069, 0.38039854499156894, 0.4353347254441928, 0.2304931996296035, 0.48019735064000013, 0.36504812492551164, 0.4131013610088409, 0.02155704840381803, 0.07652398270897848, 0.3081417932949942], 'elite_v_balance': 0.7579989333740315, 'v_rp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'init_save': [[[13, 14], [11, 7], [8, 9], [6, 8], [4, 11], [11, 7], [1, 1], [12, 12], [5, 6], [2, 10], [11, 7], [7, 3], [0, 13], [11, 7], [3, 4]], [[9, 7], [5, 1], [10, 5], [12, 8], [10, 5], [2, 2], [6, 4], [4, 10], [11, 14], [2, 2], [5, 1], [1, 3], [0, 9], [3, 13], [11, 14]], [[6, 7], [12, 1], [2, 13], [3, 6], [3, 6], [3, 6], [6, 7], [10, 10], [10, 10], [13, 0], [7, 8], [5, 5], [6, 7], [2, 13], [13, 0]]], 'elite_chrom': [[9, 7], [5, 1], [10, 5], [12, 8], [10, 5], [2, 2], [6, 4], [4, 10], [11, 14], [2, 2], [5, 1], [1, 3], [0, 9], [3, 13], [11, 14]], 'population': [[[13, 14], [11, 7], [8, 9], [6, 8], [4, 11], [11, 7], [1, 1], [12, 12], [5, 6], [2, 10], [11, 7], [7, 3], [0, 13], [11, 7], [3, 4]], [[9, 7], [1, 3], [10, 5], [0, 9], [0, 9], [2, 2], [6, 4], [4, 10], [0, 9], [2, 2], [4, 10], [1, 3], [0, 9], [1, 3], [1, 3]], [[5, 5], [3, 6], [13, 0], [3, 6], [5, 5], [3, 6], [6, 7], [14, 11], [10, 10], [4, 10], [10, 10], [4, 10], [9, 3], [2, 13], [6, 7]]]}
def checkeffective(popu1,size,num_var):
    '''
    判断候选解的有效性
    '''
    # 先清空各vm,pm的资源使用率
    for i in xrange(size):
        for j in xrange(num_var):
            popu1['v_p_cost'][i][j] = 0
            popu1['v_m_cost'][i][j] = 0
            popu1['h_p_cost'][i][j] = 0
            popu1['h_m_cost'][i][j] = 0
    # 逐一按照候选解，计算实际占用的vm,hm资源
    for i in xrange(size):
        vm_used_id = {}                                # 避免相同vm同时被映射的不同hm的错误
        for j in xrange(num_var):                      # 容器编号
            flag = True
            v_id = popu1['population'][i][j][0]
            h_id = popu1['population'][i][j][1]
            if v_id in vm_used_id:                     # 若vm已经被安排过
                if (h_id == vm_used_id[v_id]):         # 且所在的hm与安排过的hm相同，则跳过该次循环，不需要重新计算资源占用
                    continue
                else:                                  # 若hm不同于安排的hm编号，说明出现同一个vm映射到不同hm的错误，直接返回
                    print "in this chrom %s, a vm has been hosted on different hm, totally wrong!! " %popu1['population'][i]
                    return False
            else:                                                 # 其他情况包括,包括多vm映射到1个hm,按正常情况计算
                popu1['v_p_cost'][i][v_id] += popu1['c_rp'][j]
                popu1['v_m_cost'][i][v_id] += popu1['c_rm'][j]
                popu1['h_p_cost'][i][h_id] += popu1['v_rp'][v_id]
                popu1['h_m_cost'][i][h_id] += popu1['v_rm'][v_id]
                vm_used_id[v_id] = h_id
        for x in xrange(num_var):                                  # 只要超出资源限约束，即报错
            if (popu1['v_p_cost'][i][x] > popu1['v_rp'][x] or popu1['v_m_cost'][i][x] > popu1['v_rm'][x] or popu1['h_p_cost'][i][x] > 1.0 or popu1['h_m_cost'][i][x] > 1.0):
                print popu1['v_p_cost'][i][x], popu1['v_rp'][x]
                print popu1['v_m_cost'][i][x], popu1['v_rm'][x]
                print popu1['h_p_cost'][i][x]
                print popu1['h_m_cost'][i][x]
                print popu1['population'][i],x,vm_used_id       # 出现2个不同vm放于1个hm,超过hm尺寸 ，[(11, 10), (9, 2), (5, 4), (1, 3), (3, 7), (0, 11), (14, 6), (10, 14), (7, 11), (2, 0)]
                return False
    return True

if __name__ == '__main__':
    if checkeffective(popu3,3,15):
        print 'yes'
    else:
        print 'no!'