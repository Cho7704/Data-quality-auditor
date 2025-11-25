import json, os

def save_reports(report, outdir):
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir,'full_report.json'),'w') as f:
        json.dump(report,f,indent=4)