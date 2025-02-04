# Naive Bayes Classifier: Manual Implementation for Phone Example

data = [
    {"Brand": "Samsung", "Color": "Titanium Orange", "Model": "Galaxy S10", "Broken": "Yes"},
    {"Brand": "Vivo", "Color": "Black", "Model": "V20", "Broken": "No"},
    {"Brand": "iPhone", "Color": "Gold", "Model": "iPhone 12", "Broken": "Yes"},
    {"Brand": "iPhone", "Color": "White", "Model": "iPhone 11", "Broken": "No"},
    {"Brand": "Samsung", "Color": "Titanium Orange", "Model": "Galaxy Note10", "Broken": "Yes"},
    {"Brand": "Samsung", "Color": "Jade Green", "Model": "Galaxy S21", "Broken": "No"},
    {"Brand": "Vivo", "Color": "Jade Green", "Model": "V21", "Broken": "No"},
    {"Brand": "iPhone", "Color": "Black", "Model": "iPhone SE", "Broken": "No"},
    {"Brand": "Vivo", "Color": "Titanium Orange", "Model": "V23", "Broken": "Yes"},
    {"Brand": "Samsung", "Color": "Black", "Model": "Galaxy A50", "Broken": "Yes"},
]

# Input to classify
input_data = {"Brand": "Samsung", "Color": "Titanium Orange", "Model": "Galaxy S10"}

# Step 1: Calculate Prior Probabilities
def calculate_priors(data):
    total = len(data)
    broken_counts = {"Yes": 0, "No": 0}
    for item in data:
        broken_counts[item["Broken"]] += 1
    return {key: value / total for key, value in broken_counts.items()}

# Step 2: Calculate Conditional Probabilities
def calculate_conditionals(data, input_data):
    conditional_probs = {"Yes": 1, "No": 1}
    for key in input_data:
        counts = {"Yes": 0, "No": 0}
        for item in data:
            if item[key] == input_data[key]:
                counts[item["Broken"]] += 1
        total_counts = {"Yes": sum(1 for i in data if i["Broken"] == "Yes"),
                        "No": sum(1 for i in data if i["Broken"] == "No")}
        for broken in ["Yes", "No"]:
            conditional_probs[broken] *= counts[broken] / total_counts[broken] if total_counts[broken] != 0 else 0
    return conditional_probs

# Step 3: Calculate Posterior Probabilities
def calculate_posteriors(priors, conditionals):
    posteriors = {}
    for broken in priors:
        posteriors[broken] = priors[broken] * conditionals[broken]
    return posteriors

# Main Execution
priors = calculate_priors(data)
conditionals = calculate_conditionals(data, input_data)
posteriors = calculate_posteriors(priors, conditionals)

# Classify
classification = max(posteriors, key=posteriors.get)

print("")
print("Result: ")
print("Prior Probabilities:", priors)
print("Conditional Probabilities:", conditionals)
print("Posterior Probabilities:", posteriors)
print("Classification:", classification)
