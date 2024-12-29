import gradio as gr
from PIL import Image
import base64
from io import BytesIO
import os
import joblib
import pandas as pd

# Path of image (charts)
plot_folder = '../img'
question11_path = os.path.join(plot_folder, "question11.png")
question12_path = os.path.join(plot_folder, "question12.png")
question21_path = os.path.join(plot_folder, "question21.png")
question22_path = os.path.join(plot_folder, "question22.png")
question3_path = os.path.join(plot_folder, "question3.png")
question41_path = os.path.join(plot_folder, "question41.png")
question42_path = os.path.join(plot_folder, "question42.png")
question43_path = os.path.join(plot_folder, "question43.png")
question5_path = os.path.join(plot_folder, "question5.png")
question6_path = os.path.join(plot_folder, "question6.png")

# Question 1
def generate_page1():

    question1 = "Is there a correlation between wind speed/direction and PM10 levels? Does wind from certain directions bring higher pollution levels?"

    image11 = Image.open(question11_path)
    buf11 = BytesIO()
    image11.save(buf11, format='PNG')
    buf11.seek(0)
    image11_base64 = base64.b64encode(buf11.getvalue()).decode('utf-8')
    chart1 = f'<img src="data:image/png;base64,{image11_base64}" alt="heatmap" style="max-width:100%; height:auto;">'

    image12 = Image.open(question12_path)
    buf12 = BytesIO()
    image12.save(buf12, format='PNG')
    buf12.seek(0)
    image12_base64 = base64.b64encode(buf12.getvalue()).decode('utf-8')
    chart2 = f'<img src="data:image/png;base64,{image12_base64}" alt="bar_chart" style="max-width:100%; height:auto;">'

    buf11.close()
    buf12.close()
    
    comment1 = """
    <h4 style="font-size:20px; color:#004d99;">From the heatmap, the following insights can be drawn:</h4>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Wind Speed and PM10 Levels:</b> There is an observable trend where higher wind speeds (on the right side of the x-axis) generally correspond to lower average PM10 concentrations. This suggests that as wind speed increases, it helps disperse particulate matter, leading to a reduction in pollution levels in the area.<br>
    </p>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Wind Direction and PM10 Levels:</b> Certain wind directions are associated with higher PM10 levels. For instance:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;- Wind directions in the range of <b>0°-120°</b> (towards the top of the y-axis), combined with lower wind speeds, are linked to elevated PM10 concentrations.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;- Wind directions between <b>270°-300°</b> also show slightly increased PM10 levels, though less prominent than the 0°-120° range.<br>
    </p>

    <h4 style="font-size:20px; color:#004d99;">Summary:</h4>
    <p style="font-size:18px; line-height:1.6;">
    Winds coming from specific directions (<b>0°-120°</b> and to a lesser extent, <b>270°-300°</b>) are more likely to bring higher levels of particulate pollution, particularly when wind speeds are low. Both wind speed and direction influence PM10 levels, with lower wind speeds and certain wind directions being correlated with higher pollution.
    </p>
"""

    comment2 = """
    <h4 style="font-size:20px; color:#004d99;">The wind direction is categorized into bins corresponding to compass directions (e.g., N, NE, etc.).</h4>

    <h5 style="font-size:18px; color:#333366;">From the bar chart, we can observe the following:</h5>
    <p style="font-size:18px; line-height:1.6;">
    - <b>High PM10 Levels from West and Northwest:</b> The highest average PM10 concentrations are observed when the wind comes from the <b>West (W)</b> and <b>Northwest (NW)</b> directions, with averages of <b>41.5 µg/m³</b> and <b>45.9 µg/m³</b>, respectively. This suggests that winds from these directions are associated with increased PM10 levels.<br>
    </p>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Moderate PM10 Levels from North and South:</b> Winds from the <b>North (N)</b> and <b>South (S)</b> also show relatively high PM10 levels, around <b>39.7 µg/m³</b> and <b>36.3 µg/m³</b>, respectively. These directions may contribute to moderate pollution levels.<br>
    </p>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Lower PM10 Levels from East and Southeast:</b> Winds from the <b>East (E)</b> and <b>Southeast (SE)</b> bring in lower PM10 levels, averaging <b>28.6 µg/m³</b> and <b>33.1 µg/m³</b>. This could indicate fewer pollution sources or better pollutant dispersion.
    </p>

    <h4 style="font-size:20px; color:#004d99;">Summary:</h4>
    <p style="font-size:18px; line-height:1.6;">
    Winds from the <b>West</b> and <b>Northwest</b> bring the highest PM10 pollution levels. In contrast, winds from the <b>East</b> and <b>Southeast</b> are associated with cleaner air, possibly due to fewer pollution sources or more effective pollutant dispersion in those directions.
    </p>
"""

    return question1, chart1, comment1, chart2, comment2

def web_question1():

    question, chart1, comment1, chart2, comment2 = generate_page1()

    gr.Markdown(f"""<h2 style="font-size:28px; color:#333366;">Question 1: {question}</h2>""")
    gr.Markdown(f"""<h3 style="font-size:24px; color:#333333;">Answer:</h3>""")
    
    gr.HTML(chart1)
    gr.Markdown(comment1)

    gr.HTML(chart2)
    gr.Markdown(comment2)

# Question 2
def generate_page2():

    question2 = "How do extreme weather events (identified by weather_status) affect air quality parameters, and what are the lag effects on pollutant concentrations?"

    image21 = Image.open(question21_path)
    buf21 = BytesIO()
    image21.save(buf21, format='PNG')
    buf21.seek(0)
    image21_base64 = base64.b64encode(buf21.getvalue()).decode('utf-8')
    chart1 = f'<img src="data:image/png;base64,{image21_base64}" alt="heatmap" style="max-width:100%; height:auto;">'

    image22 = Image.open(question22_path)
    buf22 = BytesIO()
    image22.save(buf22, format='PNG')
    buf22.seek(0)
    image22_base64 = base64.b64encode(buf22.getvalue()).decode('utf-8')
    chart2 = f'<img src="data:image/png;base64,{image22_base64}" alt="bar_chart" style="max-width:100%; height:auto;">'
    
    buf21.close()
    buf22.close()
    
    comment = """
    <h4 style="font-size:20px; color:#004d99;">Based on the analysis of extreme weather effects on air quality parameters, we observe:</h4>

    <h5 style="font-size:18px; color:#333366;">1. Pollutant Concentration Changes:</h5>
    <p style="font-size:18px; line-height:1.6;">
    - <b>SO₂ and O₃:</b> These pollutants show the most significant increases during extreme weather (+16.69% and +17.25% respectively, <i>p</i>&lt;0.001).<br>
    - <b>Carbon Monoxide (CO):</b> Uniquely, CO shows a decrease (-4.40%), suggesting possible washout effects.<br>
    - <b>PM10 and PM2.5:</b> These show slight increases (3.14% and 4.95%) but are not statistically significant.<br>
    - Most pollutants show lower variability during extreme weather, indicating more stable concentrations.
    </p>

    <h5 style="font-size:18px; color:#333366;">2. Lag Effects After Weather Events:</h5>
    <p style="font-size:18px; line-height:1.6;">
    - Peak concentrations typically occur within the first <b>1000 hours</b> post-extreme weather.<br>
    - Different pollutants show varying recovery patterns:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;- <b>CO:</b> Stabilizes quickly after events.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;- <b>PM10 and PM2.5:</b> Gradually stabilize over <b>4000 hours</b>.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;- <b>O₃:</b> Demonstrates the most pronounced and extended fluctuations.<br>
    - 24-hour rolling averages show more stable trends compared to shorter timeframes.
    </p>

    <h4 style="font-size:20px; color:#004d99;">Summary:</h4>
    <p style="font-size:18px; line-height:1.6;">
    Extreme weather events have varying impacts on different pollutants, with <b>SO₂ and O₃</b> being most significantly affected. The lag effects persist for considerable periods (<b>1000-4000 hours</b>), suggesting the need for <b>extended monitoring and management strategies</b> post-extreme weather events. This information is crucial for public health response planning and air quality management during and after extreme weather conditions.
    </p>
"""
    
    return question2, chart1, chart2, comment

def web_question2():

    question, chart1, chart2, comment = generate_page2()

    gr.Markdown(f"""<h2 style="font-size:28px; color:#333366;">Question 2: {question}</h2>""")
    gr.Markdown(f"""<h3 style="font-size:24px; color:#333333;">Answer:</h3>""")
    
    gr.HTML(chart1)
    gr.HTML(chart2)

    gr.Markdown(comment)

# Question 3
def generate_page3():
    question3 = "Are there distinct seasonal or monthly patterns in air quality metrics?"
    
    image3 = Image.open(question3_path)
    buf3 = BytesIO()
    image3.save(buf3, format='PNG')
    buf3.seek(0)
    image3_base64 = base64.b64encode(buf3.getvalue()).decode('utf-8')
    chart1 = f'<img src="data:image/png;base64,{image3_base64}" alt="heatmap" style="max-width:100%; height:auto;">'

    buf3.close()
    
    comment = """
    <h4 style="font-size:20px; color:#004d99;">Based on the line chart, we can observe the following:</h4>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Carbon Monoxide (CO):</b> This pollutant stands out with significantly higher concentrations than the others, fluctuating around <b>300–700 µg/m³</b>. It shows a noticeable seasonal trend, with peaks around the last months of the year and lower concentrations in early summer. This suggests that CO levels might be influenced by weather conditions or emissions patterns, possibly from traffic or industrial activities.
    </p>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Other Pollutants:</b> The rest of the pollutants (PM10, PM2.5, NO₂, SO₂, O₃, and US AQI) have relatively low concentrations compared to CO, all staying below <b>100 µg/m³</b>. These pollutants exhibit smaller fluctuations and are generally stable throughout the year.
    </p>

    <h4 style="font-size:20px; color:#004d99;">Summary:</h4>
    <p style="font-size:18px; line-height:1.6;">
    Carbon Monoxide levels appear to be the primary concern due to their high concentration and seasonal spikes, while other pollutants remain relatively low and stable across the months. This could indicate targeted issues related to CO pollution sources, potentially suggesting an area for further investigation or intervention.
    </p>
"""
    
    return question3, chart1, comment

def web_question3():

    question, chart1, comment = generate_page3()

    gr.Markdown(f"""<h2 style="font-size:28px; color:#333366;">Question 3: {question}</h2>""")
    gr.Markdown(f"""<h3 style="font-size:24px; color:#333333;">Answer:</h3>""")
    gr.HTML(chart1) 
    gr.Markdown(comment)

# Question 4
def generate_page4():
    
    question4 = "What is the relationship between precipitation and air quality? Does rainfall help reduce pollutant concentrations, and if so, to what extent?"

    image41 = Image.open(question41_path)
    buf41 = BytesIO()
    image41.save(buf41, format='PNG')
    buf41.seek(0)
    image41_base64 = base64.b64encode(buf41.getvalue()).decode('utf-8')
    chart1 = f'<img src="data:image/png;base64,{image41_base64}" alt="health_effects_chart">'
    image42 = Image.open(question42_path)
    buf42 = BytesIO()
    image42.save(buf42, format='PNG')
    buf42.seek(0)
    image42_base64 = base64.b64encode(buf42.getvalue()).decode('utf-8')

    chart2 = f'<img src="data:image/png;base64,{image42_base64}" alt="health_impacts">'
    image43 = Image.open(question43_path)
    buf43 = BytesIO()
    image43.save(buf43, format='PNG')
    buf43.seek(0)
    image43_base64 = base64.b64encode(buf43.getvalue()).decode('utf-8')
    chart3 = f'<img src="data:image/png;base64,{image43_base64}" alt="pollutant_levels_health">'

    buf41.close()
    buf42.close()
    buf43.close()

    comment1 = """
    <h4 style="font-size:20px; color:#004d99;">Based on the correlation values between precipitation and pollutant levels in the charts:</h4>
    <ul style="font-size:18px; line-height:1.6;">
        <li><b>PM10 and PM2.5:</b> Weak negative correlation (-0.012 and -0.0056), suggesting minimal reduction with rainfall. There are noticeable peaks in PM10 and PM2.5 concentrations at lower precipitation values (around 0–5 mm). This might indicate that low or no rainfall correlates with higher pollutant concentrations, possibly due to stagnant air conditions allowing pollutants to accumulate.</li>
        <li><b>US AQI:</b> Slight positive correlation (0.011), suggesting rainfall may not lower AQI. The US AQI line shows significant variability, with sharp peaks and dips even at lower precipitation levels. This could indicate that air quality is influenced by other environmental factors beyond just precipitation, such as wind speed, temperature, or specific weather events.</li>
    </ul>

    <h4 style="font-size:20px; color:#004d99;">Summary:</h4>
    <p style="font-size:18px; line-height:1.6;">
    Rainfall shows minimal impact on pollutant levels.
    </p>
"""

    comment2 = """ 
    <h4 style="font-size:20px; color:#004d99;">Based on the Average pollutant levels in the chart:</h4>
    <ul style="font-size:18px; line-height:1.6;">
        <li><b>PM10:</b> lower during "Rain" (33.36 µg/m³) compared to "No Rain" (35.32 µg/m³), suggesting a slight reduction in particulate matter during rainfall.</li>
        <li><b>PM2.5:</b> lower during "Rain" (22.63 µg/m³) compared to "No Rain" (23.61 µg/m³), indicating that rainfall might help reduce smaller particulates as well.</li>
        <li><b>US AQI:</b> remains relatively stable across different rainfall events, with only minor fluctuations. This implies that rainfall does not significantly influence overall air quality (as represented by AQI).</li>
    </ul>

    <h4 style="font-size:20px; color:#004d99;">Summary:</h4>
    <p style="font-size:18px; line-height:1.6;">
    Rainfall seems to contribute slightly to the reduction of particulate pollutants (PM10 and PM2.5), but the effect is relatively minor and not strong enough to significantly impact the overall air quality (as reflected by AQI). This finding implies that while rain can help reduce pollutant levels, it may not be sufficient to substantially improve air quality on its own.
    </p>
"""
    return question4, chart1, chart2, chart3, comment1, comment2

def web_question4():

    question, chart1, chart2, chart3, comment1, comment2 = generate_page4()

    gr.Markdown(f"""<h2 style="font-size:28px; color:#333366;">Question 4: {question}</h2>""")
    gr.Markdown(f"""<h3 style="font-size:24px; color:#333333;">Answer:</h3>""")
    
    gr.HTML(chart1)
    gr.HTML(chart2)
    gr.Markdown(comment1)

    gr.HTML(chart3)
    gr.Markdown(comment2)

# Question 5
def generate_page5():
    question5 = "Are there specific times of day (morning, afternoon, evening) when pollution levels tend to be higher?"
    
    image5 = Image.open(question5_path)
    buf5 = BytesIO()
    image5.save(buf5, format='PNG')
    buf5.seek(0)
    image5_base64 = base64.b64encode(buf5.getvalue()).decode('utf-8')
    chart1 = f'<img src="data:image/png;base64,{image5_base64}" alt="pollution_by_time_of_day">'

    buf5.close()
    
    comment = """
    <h4 style="font-size:20px; color:#004d99;">Based on the chart, we can observe the following:</h4>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Ozone:</b> Ozone concentrations are highest in the morning (around <b>95.8 µg/m³</b>) and significantly decrease in the afternoon and evening (<b>31.2 µg/m³</b> and <b>37.6 µg/m³</b>, respectively). This trend could be influenced by sunlight and cloud cover variations throughout the day. Ozone formation is typically affected by sunlight, so lower afternoon and evening values may reflect cloud cover or reduced sunlight intensity as the day progresses.
    </p>

    <p style="font-size:18px; line-height:1.6;">
    - <b>PM10 and PM2.5:</b> PM10 and PM2.5 levels are somewhat consistent across different times of day, with slightly higher concentrations in the afternoon. This pattern suggests that these particulate pollutants might be less sensitive to sunlight or cloud cover and more affected by traffic or industrial activities, which remain steady throughout the day.
    </p>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Carbon Monoxide:</b> CO levels show dramatic peaks in the evening (<b>530 µg/m³</b>) and morning (<b>410 µg/m³</b>), with lower concentrations in the afternoon (<b>330 μg/m³</b>). This pattern strongly correlates with rush hour traffic patterns, reflecting vehicle emissions during peak commuting times.
    </p>
    
    <p style="font-size:18px; line-height:1.6;">
    - <b>Nitrogen and Sulfur Oxides:</b> NO₂ shows minor increases in evening hours, while SO₂ maintains stable, low concentrations throughout the day. These patterns likely reflect a combination of industrial emissions and traffic patterns, with NO₂ more responsive to vehicle emissions during peak travel times.
    </p>

    <h4 style="font-size:20px; color:#004d99;">Summary:</h4>
    <p style="font-size:18px; line-height:1.6;">
    In summary, the pollution patterns show distinct daily cycles where carbon monoxide peaks dramatically during morning and evening rush hours (<b>410-530 μg/m³</b>), while ozone shows a characteristic afternoon peak (<b>~100 μg/m³</b>) driven by sunlight intensity. Particulate matter (PM10 and PM2.5) maintains relatively stable levels throughout the day with minor fluctuations, and nitrogen/sulfur oxides show modest variations, with NO₂ slightly elevated during peak traffic periods. These patterns strongly suggest that pollution levels are primarily influenced by a combination of human activity cycles (especially traffic) and natural environmental factors like sunlight.
    </p>
"""
    
    return question5, chart1, comment

def web_question5():
    question, chart1, comment = generate_page5()

    gr.Markdown(f"""<h2 style="font-size:28px; color:#333366;">Question 5: {question}</h2>""")
    gr.Markdown(f"""<h3 style="font-size:24px; color:#333333;">Answer:</h3>""")
    gr.HTML(chart1) 
    gr.Markdown(comment)

# Question 6
def generate_page6():
    question6 = "Does a significant increase or decrease in temperature impact pollutant levels such as NO2 and ozone?"
    
    image6 = Image.open(question6_path)
    buf6 = BytesIO()
    image6.save(buf6, format='PNG')
    buf6.seek(0)
    image6_base64 = base64.b64encode(buf6.getvalue()).decode('utf-8')
    chart1 = f'<img src="data:image/png;base64,{image6_base64}" alt="temperature_daily_pattern">'

    buf6.close()

    comment = """
    <h4 style="font-size:20px; color:#004d99;">Based on the statistics and chart above, we can observe the following:</h4>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Relationship between Temperature and NO2:</b>
        <ul>
            <li>The scatter plot shows a clear <b>negative trend</b> between temperature and nitrogen dioxide (NO2) levels. As temperature increases, NO2 levels tend to decrease.</li>
            <li>The data points are more <b>dispersed</b> at lower temperatures, indicating a wider range of NO2 concentrations.</li>
            <li>At higher temperatures, the data points <b>cluster tightly</b>, suggesting a more consistent inverse relationship between temperature and NO2.</li>
        </ul>
    </p>

    <p style="font-size:18px; line-height:1.6;">
    - <b>Relationship between Temperature and Ozone:</b>
        <ul>
            <li>The scatter plot for ozone exhibits a <b>positive trend</b>, where higher temperatures correspond to higher ozone levels.</li>
            <li>The data points are more <b>scattered</b> compared to the NO2 plot, but the overall positive correlation is still evident.</li>
            <li>At the highest temperature range, the ozone levels appear to increase more sharply, indicating a potentially <b>nonlinear relationship</b>.</li>
        </ul>
    </p>

    <h4 style="font-size:20px; color:#004d99;">Summary:</h4>
    <p style="font-size:18px; line-height:1.6;">
    These visual observations highlight the contrasting relationships between temperature and the two pollutants, NO2 and ozone. Understanding these dynamics is crucial for developing targeted air quality management strategies that account for the influence of meteorological conditions on different air pollutants.
    </p>
"""
    
    return question6, chart1, comment

def web_question6():
    question, chart1, comment = generate_page6()

    gr.Markdown(f"""<h2 style="font-size:28px; color:#333366;">Question 6: {question}</h2>""")
    gr.Markdown(f"""<h3 style="font-size:24px; color:#333333;">Answer:</h3>""")
    gr.HTML(chart1)
    gr.Markdown(comment)

# Classification model
model_folder = '../model'

model_path = os.path.join(model_folder, 'classification.pkl')
scaler_path = os.path.join(model_folder, 'scaler.pkl')
label_encoder_path = os.path.join(model_folder, 'label_encoder.pkl')

loaded_model = joblib.load(model_path)
loaded_scaler = joblib.load(scaler_path)
label_encoder = joblib.load(label_encoder_path)


def predict_pipeline(precipitation, cloud_cover, wind_direction_10m, pm10, pm2_5,
                     carbon_monoxide, nitrogen_dioxide, sulphur_dioxide, ozone, us_aqi):
    # Prepare input data as a DataFrame
    input_data = {
        'precipitation': [precipitation],
        'cloud_cover': [cloud_cover],
        'wind_direction_10m': [wind_direction_10m],
        'pm10': [pm10],
        'pm2_5': [pm2_5],
        'carbon_monoxide': [carbon_monoxide],
        'nitrogen_dioxide': [nitrogen_dioxide],
        'sulphur_dioxide': [sulphur_dioxide],
        'ozone': [ozone],
        'us_aqi': [us_aqi]
    }
    input_df = pd.DataFrame(input_data)
    input_df = loaded_scaler.transform(input_df)
    # Make prediction
    prediction = loaded_model.predict(input_df)

    # Return the decoded label
    return label_encoder.inverse_transform(prediction)[0]

import random

def set_example_values():
    # Generate random example values within reasonable ranges and round them to 3 decimal places
    return [
        round(random.uniform(0, 30), 3),  # Precipitation (mm)
        round(random.uniform(0, 100), 0),  # Cloud Cover (%)
        round(random.uniform(0, 50), 3),   # Wind Direction (°)
        round(random.uniform(0, 200), 3),  # PM10 (µg/m³)
        round(random.uniform(0, 200), 3),  # PM2.5 (µg/m³)
        round(random.uniform(0, 1000), 0), # Carbon Monoxide (ppm)
        round(random.uniform(0, 200), 3),  # Nitrogen Dioxide (ppm)
        round(random.uniform(0, 60), 3),   # Sulphur Dioxide (ppm)
        round(random.uniform(0, 300), 3),  # Ozone (ppm)
        round(random.uniform(0, 200), 0)   # US AQI
    ]
   
def classifier_tab():
    gr.Markdown(f"""<h2 style="font-size:28px; color:#333366;">Weather Status Prediction</h2>""")     
    gr.Markdown("Enter air quality and weather parameters to predict the weather status.")
    
    # Example values for the input fields
    example_values = set_example_values()
    
    inputs = [
        gr.Number(label="Precipitation (mm)", info=f"Rainfall amount in millimeters (e.g., {example_values[0]})"),
        gr.Number(label="Cloud Cover (%)", info=f"Percentage of cloud cover (e.g., {example_values[1]})"),
        gr.Number(label="Wind Direction (°)", info=f"Direction of wind in degrees (e.g., {example_values[2]})"),
        gr.Number(label="PM10 (µg/m³)", info=f"Particulate matter (10 microns) (e.g., {example_values[3]})"),
        gr.Number(label="PM2.5 (µg/m³)", info=f"Particulate matter (2.5 microns) (e.g., {example_values[4]})"),
        gr.Number(label="Carbon Monoxide (ppm)", info=f"Concentration of CO (e.g., {example_values[5]})"),
        gr.Number(label="Nitrogen Dioxide (ppm)", info=f"Concentration of NO2 (e.g., {example_values[6]})"),
        gr.Number(label="Sulphur Dioxide (ppm)", info=f"Concentration of SO2 (e.g., {example_values[7]})"),
        gr.Number(label="Ozone (ppm)", info=f"Concentration of O3 (e.g., {example_values[8]})"),
        gr.Number(label="US AQI", info=f"Air Quality Index (e.g., {example_values[9]})")
    ]
    
    output_box = gr.Textbox(label="Predicted Weather Status", lines=2, placeholder="Prediction result will appear here...")
    example_button = gr.Button("Try Example")
    predict_button = gr.Button("Predict")

    predict_button.click(fn=predict_pipeline, inputs=inputs, outputs=output_box)
    example_button.click(fn=set_example_values, inputs=[], outputs=inputs)

if __name__ == "__main__":
    # Create tabs for web
    with gr.Blocks() as demo:

        gr.Markdown("""
        <h1 style="font-size:36px; text-align:center; color:#004d99; margin-bottom:20px;">
            Capydata's Data Science Website: Weather and Air Quality Analysis
        </h1>
        """)
        
        with gr.Tab("Question 1"):
            web_question1()
            
        with gr.Tab("Question 2"):
            web_question2()
            
        with gr.Tab("Question 3"):
            web_question3()
            
        with gr.Tab("Question 4"):
            web_question4() 
        
        with gr.Tab("Question 5"):
            web_question5()

        with gr.Tab("Question 6"):
            web_question6()
        
        with gr.Tab("Weather Prediction"):
            classifier_tab()
    demo.launch(share=True)