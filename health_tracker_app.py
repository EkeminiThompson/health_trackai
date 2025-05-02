from flask import Flask, request, render_template
import joblib
import numpy as np
import logging

# Initialize Flask app and logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Load models, scalers, and features
heart_model = joblib.load('heart_disease_model.pkl')
heart_scaler = joblib.load('heart_disease_scaler.pkl')
lifestyle_model = joblib.load('lifestyle_model.pkl')
lifestyle_scaler = joblib.load('lifestyle_scaler.pkl')
mental_health_model = joblib.load('mental_health_model.pkl')
mental_health_scaler = joblib.load('mental_health_scaler.pkl')
FEATURES = joblib.load('features.pkl')

# Define valid ranges for features
VALID_RANGES = {
    'age': (18, 100),
    'sex': (0, 1),
    'cp': (0, 3),
    'trestbps': (80, 200),
    'chol': (100, 600),
    'fbs': (0, 1),
    'restecg': (0, 2),
    'thalach': (60, 220),
    'exang': (0, 1),
    'oldpeak': (0, 6.2),
    'slope': (0, 2),
    'ca': (0, 4),
    'thal': (0, 3),
    'exercise': (0, 1),
    'smoking': (0, 1),
    'diet': (0, 1),
    'stress': (0, 1)
}

def validate_inputs(input_data):
    """Validate input data against acceptable ranges."""
    for feature, value in zip(FEATURES, input_data):
        min_val, max_val = VALID_RANGES[feature]
        if not (min_val <= value <= max_val):
            return False, f"Invalid value for {feature}: {value}. Must be between {min_val} and {max_val}."
    return True, ""

def generate_recommendations(heart_pred, lifestyle_pred, mental_health_pred, input_data):
    """Generate dynamic, prioritized health recommendations based on predictions and input data."""
    recommendations = {
        'heart_health': [],
        'lifestyle': [],
        'mental_health': []
    }
    
    # Map input data to feature names for easy access
    input_dict = dict(zip(FEATURES, input_data))
    
    # Heart Health Recommendations
    if heart_pred == 1:
        recommendations['heart_health'].append({
            'text': "Consult a cardiologist for a detailed heart health assessment.",
            'priority': True
        })
        if input_dict['chol'] > 240:
            recommendations['heart_health'].append({
                'text': f"Your cholesterol ({input_dict['chol']:.0f} mg/dl) is high. Reduce saturated fats and increase fiber intake.",
                'priority': True
            })
        if input_dict['trestbps'] > 140:
            recommendations['heart_health'].append({
                'text': f"Your blood pressure ({input_dict['trestbps']:.0f} mm Hg) is elevated. Monitor daily and limit salt intake.",
                'priority': True
            })
        recommendations['heart_health'].append({
            'text': "Engage in moderate aerobic exercise (e.g., brisk walking) for 150 minutes per week.",
            'priority': False
        })
    else:
        recommendations['heart_health'].append({
            'text': "Maintain regular cardiovascular exercise to keep your heart healthy.",
            'priority': False
        })
        if input_dict['chol'] > 200:
            recommendations['heart_health'].append({
                'text': f"Your cholesterol ({input_dict['chol']:.0f} mg/dl) is borderline high. Consider a diet rich in omega-3 fatty acids.",
                'priority': False
            })
    
    # Lifestyle Recommendations
    if lifestyle_pred == 0:
        if input_dict['exercise'] == 0:
            recommendations['lifestyle'].append({
                'text': "Incorporate 30 minutes of moderate exercise (e.g., cycling, swimming) 5 days a week.",
                'priority': True
            })
        if input_dict['smoking'] == 1:
            recommendations['lifestyle'].append({
                'text': "Quit smoking to significantly reduce health risks. Seek support from cessation programs.",
                'priority': True
            })
        if input_dict['diet'] == 0:
            recommendations['lifestyle'].append({
                'text': "Adopt a balanced diet with more fruits, vegetables, and whole grains.",
                'priority': True
            })
    else:
        recommendations['lifestyle'].append({
            'text': "Great job maintaining a healthy lifestyle! Keep up your exercise and balanced diet.",
            'priority': False
        })
    
    # Mental Health Recommendations
    if mental_health_pred == 0:
        recommendations['mental_health'].append({
            'text': "Practice stress-reduction techniques like meditation, deep breathing, or yoga for 10-15 minutes daily.",
            'priority': True
        })
        recommendations['mental_health'].append({
            'text': "Ensure 7-8 hours of quality sleep nightly to support mental well-being.",
            'priority': False
        })
        if input_dict['stress'] == 1:
            recommendations['mental_health'].append({
                'text': "Consider professional counseling or mindfulness apps to manage high stress levels.",
                'priority': True
            })
    else:
        recommendations['mental_health'].append({
            'text': "Maintain social connections and hobbies to support your mental health.",
            'priority': False
        })
    
    return recommendations

@app.route('/')
def home():
    """Render the home page with the input form."""
    return render_template('index.html', features=FEATURES)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle form submission and return predictions with recommendations."""
    try:
        # Get and validate input data
        input_data = [float(request.form[feature]) for feature in FEATURES]
        is_valid, error_msg = validate_inputs(input_data)
        if not is_valid:
            return render_template('index.html', features=FEATURES, error=error_msg)
        
        input_array = np.array([input_data])
        app.logger.info(f"Input data: {input_data}")
        
        # Make predictions
        heart_scaled = heart_scaler.transform(input_array)
        heart_pred = heart_model.predict(heart_scaled)[0]
        heart_conf = heart_model.predict_proba(heart_scaled)[0][int(heart_pred)] * 100
        
        lifestyle_scaled = lifestyle_scaler.transform(input_array)
        lifestyle_pred = lifestyle_model.predict(lifestyle_scaled)[0]
        lifestyle_conf = lifestyle_model.predict_proba(lifestyle_scaled)[0][int(lifestyle_pred)] * 100
        
        mental_health_scaled = mental_health_scaler.transform(input_array)
        mental_health_pred = mental_health_model.predict(mental_health_scaled)[0]
        mental_health_conf = mental_health_model.predict_proba(mental_health_scaled)[0][int(mental_health_pred)] * 100
        
        # Check for low confidence
        low_confidence_warning = ""
        if heart_conf < 50:
            low_confidence_warning += "Heart disease prediction has low confidence. Verify inputs or consult a professional. "
        if lifestyle_conf < 50:
            low_confidence_warning += "Lifestyle prediction has low confidence. Verify inputs. "
        if mental_health_conf < 50:
            low_confidence_warning += "Mental health prediction has low confidence. Verify inputs. "
        
        # Interpret predictions
        heart_result = "High risk of heart disease" if heart_pred == 1 else "Low risk of heart disease"
        lifestyle_result = "Healthy lifestyle" if lifestyle_pred == 1 else "Unhealthy lifestyle"
        mental_health_result = "Good mental health" if mental_health_pred == 1 else "High stress level"
        
        # Generate recommendations
        recommendations = generate_recommendations(heart_pred, lifestyle_pred, mental_health_pred, input_data)
        
        # Log prediction results
        app.logger.info(f"Heart Disease: {heart_result}, Confidence: {heart_conf:.2f}%")
        app.logger.info(f"Lifestyle: {lifestyle_result}, Confidence: {lifestyle_conf:.2f}%")
        app.logger.info(f"Mental Health: {mental_health_result}, Confidence: {mental_health_conf:.2f}%")
        
        return render_template('index.html', 
                             features=FEATURES, 
                             heart_result=heart_result, 
                             heart_confidence=f"{heart_conf:.2f}",
                             lifestyle_result=lifestyle_result, 
                             lifestyle_confidence=f"{lifestyle_conf:.2f}",
                             mental_health_result=mental_health_result, 
                             mental_health_confidence=f"{mental_health_conf:.2f}",
                             recommendations=recommendations,
                             low_confidence_warning=low_confidence_warning if low_confidence_warning else None)
    except Exception as e:
        error = f"Error processing input: {str(e)}"
        app.logger.error(error)
        return render_template('index.html', features=FEATURES, error=error)

if __name__ == '__main__':
    app.run(debug=True)