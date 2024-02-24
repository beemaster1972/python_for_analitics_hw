def calc_income_by_month(dates: list, incomes:list) -> dict:
    temp = list(zip(dates,incomes))
    result ={}
    for k,v in temp:
        result[k.split('-')[1]] = result.get(k.split('-')[1],0) + v
    return result




print(calc_income_by_month(dates = ['2021-11-01','2021-11-02','2021-11-03'], incomes = [100, 200, 300]))