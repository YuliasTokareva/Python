# базовые значения тарифа
bazovaya_summa = 24.99
vklucheno_minutes = 60
vklucheno_sms = 30
vklucheno_gb = 1

# стоимость дополнительных услуг
vklucheno_minutes = 0.89
stoimost_sms = 0.59
stoimost_mb = 0.79

# налог
nalog_protsent = 2

# данные
ispolzovano_minutes = int(input("Сколько минут вы использовали за месяц? "))
ispolzovano_sms = int(input("Сколько СМС вы отправили за месяц? "))
ispolzovano_mb = int(input("Сколько МБ интернета вы использовали за месяц? (1 ГБ = 1024 МБ) "))

print("=== РАСЧЁТ СЧЁТА ЗА ТЕЛЕФОН ===")
print("Базовая сумма тарифа:", f"{bazovaya_summa:.2f}", "руб.")

# доп минуты
dop_minutes = 0
if ispolzovano_minutes > vklucheno_minutes:
    dop_minutes = ispolzovano_minutes - vklucheno_minutes
    stoimost_dop_minutes = dop_minutes * vklucheno_minutes
    print("Дополнительные минуты:", dop_minutes, "шт. →", f"{stoimost_dop_minutes:.2f}", "руб.")
else:
    stoimost_dop_minutes = 0.0

# доп СМС
dop_sms = 0
if ispolzovano_sms > vklucheno_sms:
    dop_sms = ispolzovano_sms - vklucheno_sms
    stoimost_dop_sms = dop_sms * stoimost_sms
    print("Дополнительные СМС:", dop_sms, "шт. →", f"{stoimost_dop_sms:.2f}", "руб.")
else:
    stoimost_dop_sms = 0.0

# доп трафик
dop_mb = 0
vklucheno_v_mb = vklucheno_gb * 1024
if ispolzovano_mb > vklucheno_v_mb:
    dop_mb = ispolzovano_mb - vklucheno_v_mb
    stoimost_dop_mb = dop_mb * stoimost_mb
    print("Дополнительный интернет (МБ):", dop_mb, "МБ →", f"{stoimost_dop_mb:.2f}", "руб.")
else:
    stoimost_dop_mb = 0.0

# общая сумма до налога
summa_do_naloga = bazovaya_summa + stoimost_dop_minutes + stoimost_dop_sms + stoimost_dop_mb

# налог
nalog = summa_do_naloga * nalog_protsent / 100
print("Налог (2%):", f"{nalog:.2f}", "руб.")

# итог
itogo = summa_do_naloga + nalog
print("ИТОГО К ОПЛАТЕ:", f"{itogo:.2f}", "руб.")