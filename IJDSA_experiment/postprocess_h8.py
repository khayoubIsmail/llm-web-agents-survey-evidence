import argparse
import csv
import os

def process_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        fieldnames = f.readline().strip().split(',')
        
    if not reader: return
    if 'supported_field_count' not in reader[0]: return
    
    for row in reader:
        try:
            sup = float(row.get('supported_field_count') or 0)
            unsup = float(row.get('unsupported_field_count') or 0)
            non_schema = float(row.get('non_schema_field_count') or 0)
        except ValueError:
            sup, unsup, non_schema = 0.0, 0.0, 0.0
            
        total_schema = sup + unsup
        total_all = total_schema + non_schema
        
        row['unsupported_value_rate'] = str(unsup / total_schema) if total_schema > 0 else "0.0"
        row['non_schema_field_rate'] = str(non_schema / total_all) if total_all > 0 else "0.0"
        
    if 'unsupported_value_rate' not in reader[0]:
        new_fields = list(reader[0].keys())
    else:
        new_fields = list(reader[0].keys())
        
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_fields)
        writer.writeheader()
        writer.writerows(reader)
    print(f"Updated {filepath}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='results directory')
    parser.add_argument('--in-place', action='store_true')
    args = parser.parse_args()
    
    if args.in_place:
        for f in os.listdir(args.dir):
            if f.endswith('.csv'):
                process_csv(os.path.join(args.dir, f))

if __name__ == "__main__":
    main()
