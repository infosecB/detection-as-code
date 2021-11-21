import yaml
import os
import glob
from jinja2 import Template


ss_template = """
[{{ title }}]
alert.expires = 5m
alert.suppress = 1
alert.suppress.period = 60m
alert.track = 1
counttype = number of events
cron_schedule = {{ cron }}
description = Detects a second malicious IP.
enableSched = 1
quantity = 0
relation = greater than
search = {{ search }}

"""


def priority_to_cron(priority):
    if priority == "low":
        return "0 */4 * * *"
    elif priority == "high":
        return "*/15 * * * *"
    elif priority == "critical":
        return "*/5 * * * *"
    else:
        return "0 * * * *"


t = Template(ss_template)

savedsearch_content = ""

rules = yaml.safe_load(open("out.yaml"))
for rule in rules:
    if rule["status"] == "stable":
        print("Creating alert for " + rule["title"])
        savedsearch_content += t.render(
            title=rule["title"], search=rule["rule"][0], cron=priority_to_cron("normal")
        )
    else:
        print(
            'The rule "'
            + rule["title"]
            + '" status is set to '
            + rule["status"]
            + ", skipping."
        )

f = open("savedsearches.conf", "w")
f.write(savedsearch_content)
f.close()
