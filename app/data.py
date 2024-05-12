import json
import re
import os
import glob
from pathlib import Path

chardir = "characters"
skills = None

def get_all_chars():
	files = glob.glob(f"data/{chardir}/*.json*")
	out = []
	for f in files:
		cname = Path(f).stem
		out.append(import_charsheet(cname))
	out = sorted(out, key=lambda d: d['name'])
	return out
	# return [os.path.basename(f) for f in files]

def import_charsheet(n):
	out = {}
	try:
		with open(f"data/{chardir}/{n}.json", 'r') as f:
			out = json.load(f)
	except:
		return None
	if not os.path.isfile(f"app/static/{out['thumbnailPath']}"):
		out['thumbnailPath'] = "images/characters/default.jpg"
	out['totalArmorPoints'] = calc_armor(out['armor'])
	out['_items'] = out['items']
	allskills = load_skills()
	out['mappedSkills'] = {
		'unknown' : []
	}
	for s in out['skills']:
		found = False
		for k,d in allskills.items():
			if s in d['skills']:
				found = True
				if k not in out['mappedSkills']:
					out['mappedSkills'][k] = []
				out['mappedSkills'][k].append(parse_camel_cased(s))
		if False == found:
			out['mappedSkills']['unknown'].append(s)
	out['selfLink'] = f"/characters/{n.replace(' ','-')}"
	out['allskills'] = load_skills()
	return out

def load_skills():
	global skills
	if None == skills:
		try:
			with open(f"data/skills.json", 'r') as f:
				skills = json.load(f)
		except:
			return skills
	return skills

def calc_armor(armoritems):
	total = 0
	for a in armoritems:
		total += a['armorPoints']
	return total

def parse_camel_cased(w):
	w = w[0].upper() + w[1:]
	words = re.findall('[A-Z][^A-Z]*', w)
	return ' '.join(words)