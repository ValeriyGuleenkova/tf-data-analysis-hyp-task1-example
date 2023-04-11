import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

chat_id = 215606022

#x - контроль, y - тест
def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    _,p_val = proportions_ztest([x_success,y_success],[x_cnt,y_cnt], alternative = 'smaller')
    sgn_lvl = 0.08
    print(p_val)
    #если p_value маленькое, то отвергаем гипотезу, то есть на тесте лучше
    #вопрос в задании "отклонить ли гипотезу "на тесте лучше" "
    if(p_val > sgn_lvl): #при таком знаке 1/3, при противоположном 2/3
        return False
    return True 
