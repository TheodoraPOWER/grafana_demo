
import json

def flatten_json():
    input_path = '/home/jwcastillo/Develop/2025/Theodora/grafana_demo/nics_demo.json'
    output_path = '/home/jwcastillo/Develop/2025/Theodora/grafana_demo/nics_demo_flat.json'

    try:
        with open(input_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {input_path}")
        return

    flat_data = []
    for function in data:
        function_name = function.get('function')
        function_score = function.get('function_score')
        if not function.get('categories'):
            continue
        for category in function.get('categories', []):
            category_name = category.get('category')
            category_score = category.get('category_score')
            if not category.get('subcategories'):
                continue
            for subcategory in category.get('subcategories', []):
                # Create a copy to avoid modifying the original dict
                sub_copy = subcategory.copy()

                # Extract nested scores and maturity levels
                policy_maturity = sub_copy.pop('policy_maturity', None)
                policy_score = sub_copy.pop('policy_score', None)
                process_maturity = sub_copy.pop('process_maturity', None)
                process_score = sub_copy.pop('process_score', None)
                implementation_maturity = sub_copy.pop('implementation_maturity', None)
                implementation_score = sub_copy.pop('implementation_score', None)
                measured_maturity = sub_copy.pop('measured_maturity', None)
                measured_score = sub_copy.pop('measured_score', None)
                managed_maturity = sub_copy.pop('managed_maturity', None)
                managed_score = sub_copy.pop('managed_score', None)

                flat_subcategory = {
                    'function': function_name,
                    'function_score': float(function_score) if function_score else None,
                    'category': category_name,
                    'category_score': float(category_score) if category_score else None,
                    'subcategory': sub_copy.get('subcategory'),
                    'subcategory_score': float(sub_copy.get('subcategory_score')) if sub_copy.get('subcategory_score') else None,
                    'policy_maturity': policy_maturity,
                    'policy_score': float(policy_score) if policy_score else None,
                    'process_maturity': process_maturity,
                    'process_score': float(process_score) if process_score else None,
                    'implementation_maturity': implementation_maturity,
                    'implementation_score': float(implementation_score) if implementation_score else None,
                    'measured_maturity': measured_maturity,
                    'measured_score': float(measured_score) if measured_score else None,
                    'managed_maturity': managed_maturity,
                    'managed_score': float(managed_score) if managed_score else None,
                    'estimated_level_of_effort_in_hours': int(sub_copy.get('estimated_level_of_effort_in_hours')) if sub_copy.get('estimated_level_of_effort_in_hours') else None,
                    'artifacts_needed': sub_copy.get('artifacts_needed'),
                    'informative_references': sub_copy.get('informative_references'),
                    'risk_register': sub_copy.get('risk_register'),
                    'artifacts': sub_copy.get('artifacts'),
                    'artifacts_placed_in_folder': sub_copy.get('artifacts_placed_in_folder'),
                    'assessment_results': sub_copy.get('assessment_results'),
                    'assessment_reccommendations': sub_copy.get('assessment_reccommendations')
                }
                flat_data.append(flat_subcategory)

    with open(output_path, 'w') as f:
        json.dump(flat_data, f, indent=2)
    
    print(f"Successfully created flattened JSON at {output_path}")

if __name__ == '__main__':
    flatten_json()
