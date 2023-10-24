import json
from instances import cpu_util, memory_usage, root_disk_usage, data_disk_usage

widget_list = []
cpu_list = []
memory_list = []
disk_used_list = []
data_used_list = []

for instance in cpu_util:
    cpu = ["AWS/EC2", "CPUUtilization", "InstanceId", instance]
    cpu_list.append(cpu)

cpu_widget = {
    "type": "metric",
    "x": 0,
    "y": 0,
    "width": 12,
    "height": 6,
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": cpu_list,
        "region": "us-west-2",
        "title": "CPU Utilization"
    }
}

widget_list.append(cpu_widget)

for instance in memory_usage:
    memory = ["CWAgent", "mem_used_percent", "InstanceId", instance]
    memory_list.append(memory)

memory = {
    "type": "metric",
    "x": 0,
    "y": 0,
    "width": 12,
    "height": 6,
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": memory_list,
        "region": "us-west-2",
        "title": "Memory Usage"
    }
}

widget_list.append(memory)

for instance in root_disk_usage:
    disk_used = [ "CWAgent", "disk_used_percent", "InstanceId", instance, "device", "nvme0n1p1", "fstype", "xfs", "path", "/"]
    disk_used_list.append(disk_used)

disk = {
    "type": "metric",
    "x": 0,
    "y": 0,
    "width": 12,
    "height": 6,
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": disk_used_list,
        "region": "us-west-2",
        "title": "Root Disk Usage"
    }
}
widget_list.append(disk)

for instance in data_disk_usage:
    data_disk_used = ["CWAgent", "disk_used_percent", "InstanceId", instance, "device", "nvme1n1", "fstype", "xfs", "path", "/DATA"]
    data_used_list.append(data_disk_used)

data = {
    "type": "metric",
    "x": 0,
    "y": 0,
    "width": 12,
    "height": 6,
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": data_used_list,
        "region": "us-west-2",
        "title": "Data Disk Usage"
    }
}

widget_list.append(data)

# Create the JSON file from the list of widgets.
dashboard_template = {
    "widgets": widget_list
}


json_template = json.dumps(dashboard_template, indent=4)


with open("dashboard-template.json", "w") as file:
    file.write(json_template)
