def perfometer_processor_utility(row, check_command, perf_data):
        util=max(i[1] for i in perf_data)
        color = "#60c080"
        return "%d %%" % util, perfometer_linear(util, color)

perfometers['check_mk-processor_utility'] = perfometer_processor_utility

