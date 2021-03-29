import yaml
import ansible.inventory
from ansible_playbook_runner import Runner
cont = input("Enter container Name: " ) or "newCont"
image= input("Enter Image name: ") or "centos"
version= input("Enter Version: ") or "latest"
state = input("Enter state: ") or "started"
port = input("Enter port to export: ") or "80"

with open(r'./vars.yml') as f:
    doc = yaml.full_load(f)

doc['image']= image
doc['version']= version
doc['state']= state
doc['container']= cont
doc['port']= port

with open('./vars.yml', 'w') as f:
    yaml.dump(doc, f)

Runner(["localhost"], "/wp1/docker.yml").run()
