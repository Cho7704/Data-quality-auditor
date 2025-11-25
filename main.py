from auditor import run_audit
from loader import load_csv
from report import save_reports

def main():
    df=load_csv('../data/sample.csv')
    report=run_audit(df)
    save_reports(report, '../output')

if __name__=='__main__': main()