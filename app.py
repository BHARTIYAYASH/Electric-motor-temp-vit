from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the model
try:
    model = joblib.load('best_model.pkl')
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Warning: best_model.pkl not found. Please ensure the file exists in the project directory.")
    model = None

FEATURE_NAMES = ['u_q', 'coolant', 'stator_winding', 'u_d', 'stator_tooth', 
                 'motor_speed', 'i_d', 'i_q', 'stator_yoke', 'torque']

@app.route('/')
def home():
    """Home route that renders the main prediction page"""
    return render_template('manual_predict.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    """
    Prediction route that processes form data and returns prediction
    """
    try:
        # Collect form values as float inputs
        u_q = float(request.form['u_q'])
        coolant = float(request.form['coolant'])
        stator_winding = float(request.form['stator_winding'])
        u_d = float(request.form['u_d'])
        stator_tooth = float(request.form['stator_tooth'])
        motor_speed = float(request.form['motor_speed'])
        i_d = float(request.form['i_d'])
        i_q = float(request.form['i_q'])
        stator_yoke = float(request.form['stator_yoke'])
        torque = float(request.form['torque'])
        
        print(f"Received values: u_q={u_q}, coolant={coolant}, stator_winding={stator_winding}, "
              f"u_d={u_d}, stator_tooth={stator_tooth}, motor_speed={motor_speed}, "
              f"i_d={i_d}, i_q={i_q}, stator_yoke={stator_yoke}, torque={torque}")
        
        input_data = pd.DataFrame({
            'u_q': [u_q],
            'coolant': [coolant],
            'stator_winding': [stator_winding],
            'u_d': [u_d],
            'stator_tooth': [stator_tooth],
            'motor_speed': [motor_speed],
            'i_d': [i_d],
            'i_q': [i_q],
            'stator_yoke': [stator_yoke],
            'torque': [torque]
        })

        print(f"Input DataFrame shape: {input_data.shape}")
        print(f"Input DataFrame columns: {input_data.columns.tolist()}")
        
        # Make prediction
        if model is not None:
            try:
                prediction = model.predict(input_data)[0]
                prediction_text = f"Predicted Rotor Temperature: {prediction:.2f}°C"
                print(f"Prediction successful: {prediction}")
            except Exception as e:
                print(f"Prediction with DataFrame failed: {e}")
                try:
                    prediction = model.predict(input_data.values)[0]
                    prediction_text = f"Predicted Rotor Temperature: {prediction:.2f}°C"
                    print(f"Prediction with array successful: {prediction}")
                except Exception as e2:
                    print(f"Prediction with array also failed: {e2}")
                    prediction_text = f"Prediction failed: {str(e2)}"
        else:
            demo_pred = u_q + (motor_speed/100) + abs(i_q)*0.5
            prediction_text = f"Model not loaded. Demo prediction: {demo_pred:.2f}°C"
            print(f"Using demo prediction: {demo_pred}")
        
        print(f"Final prediction text: {prediction_text}")
        
        # Return the result to HTML
        return render_template('manual_predict.html', 
                             prediction_text=prediction_text,
                             u_q=u_q,
                             coolant=coolant,
                             stator_winding=stator_winding,
                             u_d=u_d,
                             stator_tooth=stator_tooth,
                             motor_speed=motor_speed,
                             i_d=i_d,
                             i_q=i_q,
                             stator_yoke=stator_yoke,
                             torque=torque)
    
    except ValueError as e:
        prediction_text = "Error: Please enter valid numeric values for all fields."
        print(f"ValueError: {e}")
        return render_template('manual_predict.html', prediction_text=prediction_text)
    
    except Exception as e:
        prediction_text = f"Error occurred during prediction: {str(e)}"
        print(f"General error: {e}")
        return render_template('manual_predict.html', prediction_text=prediction_text)

@app.route('/manual_predict')
def manual_predict():
    return render_template('manual_predict.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
