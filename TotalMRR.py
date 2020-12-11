import chartmogul

config = chartmogul.Config('0bf0c27f6492ce2ce8d88c5ca9ea6bba', '7fa2c0e0515d1b916997a42db98fd675')

data = chartmogul.Metrics.mrr(
    config,
    start_date="2019-01-01",
    end_date="2019-04-30",
    interval="month")

jsonMsg = data.value
print(jsonMsg, end="\n\n")
