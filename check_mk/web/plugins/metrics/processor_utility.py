metric_info["numa0"] = {
    "title": _("Processor utility on NUMA node 0"),
    "unit": "%",
    "color": "#0000ff",
}
metric_info["numa1"] = {
    "title": _("Pocessor utility on NUMA node 1"),
    "unit": "%",
    "color": "#00ff00",
}

graph_info.append({
    "title": _("Processor Utility"),
    "metrics": [
        ( "numa0", "line" ),
        ( "numa1", "line" ),
    ],
    #"scalars": [
    #    "numa0:warn",
    #    "numa0:crit",
    #],
})
