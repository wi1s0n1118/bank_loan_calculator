#!/usr/bin/env python
###################################################################################################
#
# Title: bank_loan_calculator.py
# Usage: To make a calculation for the bank loan
# Author: Wi1s0n
# Date: 2021/09/15
#
###################################################################################################

import prettytable as pt

class LoanCalculation(object):
    """
    [住房贷款计算器]
    1、支持等额本息、等额本金两种计算方式；
    2、还款周期以月为单位，输出当前期数、月供总额、月供本金、月供利息、剩余本金；
    3、交互式菜单输入，并以表格形式显示结果，增加可读性。
    """
    def __init__(self):
        """
        @param installment_list: 月供清单
        @param total_payment: 还款总额
        @param total_interest: 利息总额
        """
        self.installment_list = []
        self.total_payment = 0
        self.total_interest = 0

    def equal_interest(self,P,R,N):
        """等额本息"""
        Pi = P
        A = (P*R/1200*(1+R/1200)**N)/((1+R/1200)**N-1)
        for i in range(1,N+1):
            B = (P*R/1200*(1+R/1200)**(i-1))/((1+R/1200)**N-1)
            r = A-B
            Pi -= B
            installment_dict = {"time_num":i,
                                "monthly_payment":round(A,2),
                                "monthly_principal":round(B,2),
                                "monthly_interest":round(r,2),
                                "rest_loan":round(Pi,2)}
            self.installment_list.append(installment_dict)
        self.total_payment = (round(sum([x["monthly_payment"] for x in self.installment_list])))
        self.total_interest = (round(sum([x["monthly_interest"] for x in self.installment_list])))

    def equal_principal(self,P,R,N):
        """等额本金"""
        B = P/N
        for i in range(1,N+1):
            A = P/N+(P-P/N*(i-1))*R/1200
            r = A-B
            installment_dict = {"time_num":i,
                                "monthly_payment":round(A,2),
                                "monthly_principal":round(B,2),
                                "monthly_interest":round(r,2),
                                "rest_loan":round(P-P/N*i,2)}
            self.installment_list.append(installment_dict)
        self.total_payment = (round(sum([x["monthly_payment"] for x in self.installment_list])))
        self.total_interest = (round(sum([x["monthly_interest"] for x in self.installment_list])))

    def standardized_output(self):
        """输出表格"""
        tb = pt.PrettyTable()
        tb.field_names = list(self.installment_list[0].keys())
        for i in self.installment_list:
            tb.add_row(list(i.values()))
        self.installment_list.clear() # 清空列表
        return tb

    @staticmethod
    def print_menu():
        """程序菜单提示"""
        main_menu = pt.PrettyTable()
        main_menu.field_names = ["The Bank Loan Calculator V1.0"]
        main_menu.add_row(["[1] Equality principal and interest"+" "*18])
        main_menu.add_row(["[2] Equality principal"+" "*32])
        main_menu.add_row(["[0] quit"+" "*46])
        main_menu.junction_char = "#"
        main_menu.horizontal_char = "*"
        main_menu.vertical_char = "|"
        return main_menu

    @staticmethod
    def option_info(opcode,P,R,N):
        """用户选项信息"""
        user_scheme_info = pt.PrettyTable()
        user_scheme_info.field_names = ["Loan scheme","Principal (RMB)","Annual interest rate (%)","Loan time (month)"]
        if opcode == 1:
            user_scheme_info.add_row(["Equality principal&interest",P,R,N])
        else:
            user_scheme_info.add_row(["Equality principal",P,R,N])
        return user_scheme_info

    def show_calculation(self,opcode,P,R,N):
        """计算结果显示"""
        print("Your loan scheme details is as follow:")
        print(self.option_info(opcode,P,R,N))
        if opcode == 1:
            self.equal_interest(P,R,N)
            print(self.standardized_output())
            print("Total Payment:{},Total Interest:{}".format(self.total_payment,self.total_interest))
        else:
            self.equal_principal(P,R,N)
            print(self.standardized_output())
            print("Total Payment:{},Total Interest:{}".format(self.total_payment,self.total_interest))

    def input_control(self):
        """用户输入控制"""
        while True:
            try:
                print(self.print_menu())
                opcode = int(input("Please input the option you want:"))
                if opcode in [0,1,2]:
                    if opcode == 0:
                        return
                    P = float(input("Please input the principal:"))
                    R = float(input("Please input the annual interest rate (%):"))
                    N = int(input("Please input the loan time (month):"))
                else:
                    print("[Warning] Invalid value,motherfucker!Please re-type your information.")
                    continue
            except ValueError:
                print("[Warning] Invalid value,motherfucker!Please re-type your information.")
                continue
            self.show_calculation(opcode,P,R,N)


if __name__ == '__main__':
    wilson = LoanCalculation()
    wilson.input_control()
    print("Goodbye,gentlemen！")

