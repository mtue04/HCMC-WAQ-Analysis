
# def get_aqi_advice(number, aqi):

#     # Generate the response using the LLM
#     llm = llm_model.with_structured_output(schema=AQIAdvice)

#     chain = prompt_template | llm

#     res = chain.invoke({"number": number,
#                         "aqi":aqi,
#                         "aqi_classify": classify_aqi(aqi)})
#     return res.advice

# def predict_aqi(model_path, pred_days=3):
#     if os.path.exists(model_path):
#         forecaster = joblib.load(model_path)
#     else:
#         return False

#     pred_range = pred_days * 24  # Giả sử dữ liệu theo giờ
#     fh = ForecastingHorizon(np.arange(1, pred_range + 1), is_relative=True)
#     y_pred = forecaster.predict(fh)

#     overall_avg = np.mean(y_pred)

#     return y_pred, overall_avg

# def plot_aqi(pred_days, model_path='../model/ts_forecasting_model.pkl'):
#     y_pred, avg = predict_aqi(model_path, pred_days)

#     # Create DataFrame for predictions
#     df = pd.DataFrame({
#         'time': pd.to_datetime(y_pred.index),
#         'AQI': y_pred.values
#     })

#     advice = get_aqi_advice(pred_days, avg)  # Get the advice text

#     # Classify AQI levels
#     labels = [classify_aqi(aqi) for aqi in df['AQI']]

#     # Plotly graph
#     fig = go.Figure()

#     # Add AQI prediction trace
#     fig.add_trace(go.Scatter(
#         x=df['time'],
#         y=df['AQI'],
#         mode='lines',
#         name='Predicted AQI',
#         hovertemplate=(
#             'Time: %{x|%Y-%m-%d %H:%M}<br>' +
#             'AQI: %{y}<br>' +
#             'Level: %{text}<extra></extra>'
#         ),
#         text=labels
#     ))

#     # Update layout for better readability
#     fig.update_layout(
#         title=f'Predicted AQI for Ho Chi Minh City ({pred_days} Days)',
#         xaxis_title='Time',
#         yaxis_title='AQI',
#         template='plotly',
#         xaxis=dict(tickformat="%Y-%m-%d"),
#         height=600,
#         width=800
#     )

#     # Return the figure and the advice as text
#     return fig, advice

# def plot_aqi(pred_days, model_path='../model/ts_forecasting_model.pkl'):
#     try:
#         # Predict AQI and get the average
#         y_pred, avg = predict_aqi(model_path, pred_days)

#         # Ensure predictions are valid
#         if y_pred is None or len(y_pred) == 0:
#             raise ValueError("Prediction data is empty or invalid. Check the model or input.")

#         # Convert predictions to a DataFrame
#         if hasattr(y_pred, 'index') and hasattr(y_pred, 'values'):
#             # If y_pred has an index and values (e.g., a Pandas Series)
#             df = pd.DataFrame({
#                 'time': pd.to_datetime(y_pred.index),
#                 'AQI': y_pred.values
#             })
#         else:
#             # If y_pred is a plain array, generate a time index
#             time_index = pd.date_range(
#                 start=pd.Timestamp.now(), periods=len(y_pred), freq='H'
#             )
#             df = pd.DataFrame({
#                 'time': time_index,
#                 'AQI': y_pred
#             })

#         # Generate advice
#         advice = get_aqi_advice(pred_days, avg)

#         # Classify AQI levels
#         labels = [classify_aqi(aqi) for aqi in df['AQI']]

#         # Create Plotly figure
#         fig = go.Figure()

#         # Add AQI prediction trace
#         fig.add_trace(go.Scatter(
#             x=df['time'],
#             y=df['AQI'],
#             mode='lines',
#             name='Predicted AQI',
#             hovertemplate=(
#                 'Time: %{x|%Y-%m-%d %H:%M}<br>' +
#                 'AQI: %{y}<br>' +
#                 'Level: %{text}<extra></extra>'
#             ),
#             text=labels
#         ))

#         # Update layout for better readability
#         fig.update_layout(
#             title=f'Predicted AQI for Ho Chi Minh City ({pred_days} Days)',
#             xaxis_title='Time',
#             yaxis_title='AQI',
#             template='plotly',
#             xaxis=dict(tickformat="%Y-%m-%d"),
#             height=600,
#             width=800
#         )

#         return fig, advice

#     except Exception as e:
#         print(f"An error occurred in plot_aqi: {e}")
#         return None, f"Error generating AQI plot: {str(e)}"

def plot_aqi(pred_days, model_path='../model/ts_forecasting_model.pkl'):
    try:
        # Predict AQI and get the average
        y_pred, avg = predict_aqi(model_path, pred_days)

        # Ensure predictions are valid
        if y_pred is None or len(y_pred) == 0:
            raise ValueError("Prediction data is empty or invalid. Check the model or input.")

        # Convert predictions to a DataFrame
        if hasattr(y_pred, 'index') and hasattr(y_pred, 'values'):
            # If y_pred has an index and values (e.g., a Pandas Series)
            df = pd.DataFrame({
                'time': pd.to_datetime(y_pred.index),
                'AQI': y_pred.values
            })
        else:
            # If y_pred is a plain array, generate a time index
            time_index = pd.date_range(
                start=pd.Timestamp.now(), periods=len(y_pred), freq='H'
            )
            df = pd.DataFrame({
                'time': time_index,
                'AQI': y_pred
            })

        # Classify AQI levels
        labels = [classify_aqi(aqi) for aqi in df['AQI']]

        # Create Plotly figure
        fig = go.Figure()

        # Add AQI prediction trace
        fig.add_trace(go.Scatter(
            x=df['time'],
            y=df['AQI'],
            mode='lines',
            name='Predicted AQI',
            hovertemplate=(
                'Time: %{x|%Y-%m-%d %H:%M}<br>' +
                'AQI: %{y}<br>' +
                'Level: %{text}<extra></extra>'
            ),
            text=labels
        ))

        # Update layout for better readability
        fig.update_layout(
            title=f'Predicted AQI for Ho Chi Minh City ({pred_days} Days)',
            xaxis_title='Time',
            yaxis_title='AQI',
            template='plotly',
            xaxis=dict(tickformat="%Y-%m-%d"),
            height=600,
            width=800
        )

        return fig

    except Exception as e:
        print(f"An error occurred in plot_aqi: {e}")
        return None


#     with gr.Column():
#         with gr.Row():
#             # Slider to select number of days to predict
#             min_days = gr.Slider(
#                 minimum=1,
#                 maximum=7,
#                 value=7,
#                 step=1,
#                 label="Days to Predict"
#             )

#         btn = gr.Button(value="Update Prediction")
#         map = gr.Plot(label="Predicted AQI Visualization")

#     # Load plot when the page is loaded
#     demo.load(plot_aqi, [min_days], map)

#     # Update the plot when the button is clicked
#     btn.click(plot_aqi, [min_days], map)

# # # Launch Gradio interface
# # demo.launch()

# """# Classification model"""

# class WeatherAdvice(BaseModel):
#     weather_status: str = Field(description="The weather status given")
#     advice: str = Field(description="The advice activity for the weather status")


# prompt_template = ChatPromptTemplate.from_template(
#     """
#     In the context of the weather status: {weather_status}, suggest some good activities to do or provide advice on what to wear when facing this weather condition.
#     (Write your response in a friendly tone like on TV weather forecast show.)
#     """
# )


# def get_weather_advice(weather_status):

#     # Generate the response using the LLM
#     llm = llm_model.with_structured_output(schema=WeatherAdvice)

#     chain = prompt_template | llm

#     res = chain.invoke({"weather_status": weather_status})
#     return res.advice

# model_folder = '../model'

# model_path = os.path.join(model_folder, 'classification.pkl')
# scaler_path = os.path.join(model_folder, 'scaler.pkl')
# label_encoder_path = os.path.join(model_folder, 'label_encoder.pkl')

# loaded_model = joblib.load(model_path)
# loaded_scaler = joblib.load(scaler_path)
# label_encoder = joblib.load(label_encoder_path)


# def predict_pipeline(precipitation, cloud_cover, wind_direction_10m, pm10, pm2_5,
#                      carbon_monoxide, nitrogen_dioxide, sulphur_dioxide, ozone, us_aqi):
#     # Prepare input data as a DataFrame
#     input_data = {
#         'precipitation': [precipitation],
#         'cloud_cover': [cloud_cover],
#         'wind_direction_10m': [wind_direction_10m],
#         'pm10': [pm10],
#         'pm2_5': [pm2_5],
#         'carbon_monoxide': [carbon_monoxide],
#         'nitrogen_dioxide': [nitrogen_dioxide],
#         'sulphur_dioxide': [sulphur_dioxide],
#         'ozone': [ozone],
#         'us_aqi': [us_aqi]
#     }
#     input_df = pd.DataFrame(input_data)
#     input_df = loaded_scaler.transform(input_df)
#     # Make prediction
#     prediction = loaded_model.predict(input_df)

#     # Return the decoded label
#     return label_encoder.inverse_transform(prediction)[0]

# def set_example_values():
#     # Generate random example values within reasonable ranges and round them to 3 decimal places
#     return [
#         round(random.uniform(0, 30), 3),  # Precipitation (mm)
#         round(random.uniform(0, 100), 0),  # Cloud Cover (%)
#         round(random.uniform(0, 50), 3),   # Wind Direction (°)
#         round(random.uniform(0, 200), 3),  # PM10 (µg/m³)
#         round(random.uniform(0, 200), 3),  # PM2.5 (µg/m³)
#         round(random.uniform(0, 1000), 0), # Carbon Monoxide (ppm)
#         round(random.uniform(0, 200), 3),  # Nitrogen Dioxide (ppm)
#         round(random.uniform(0, 60), 3),   # Sulphur Dioxide (ppm)
#         round(random.uniform(0, 300), 3),  # Ozone (ppm)
#         round(random.uniform(0, 200), 0)   # US AQI
#     ]

# def classifier_tab():
#     gr.Markdown(f"""<h2 style="font-size:28px; color:#333366;">Weather Status Prediction</h2>""")
#     gr.Markdown("Enter air quality and weather parameters to predict the weather status.")

#     # Example values for the input fields
#     example_values = set_example_values()

#     inputs = [
#         gr.Number(label="Precipitation (mm)", info=f"Rainfall amount in millimeters (e.g., {example_values[0]})"),
#         gr.Number(label="Cloud Cover (%)", info=f"Percentage of cloud cover (e.g., {example_values[1]})"),
#         gr.Number(label="Wind Direction (°)", info=f"Direction of wind in degrees (e.g., {example_values[2]})"),
#         gr.Number(label="PM10 (µg/m³)", info=f"Particulate matter (10 microns) (e.g., {example_values[3]})"),
#         gr.Number(label="PM2.5 (µg/m³)", info=f"Particulate matter (2.5 microns) (e.g., {example_values[4]})"),
#         gr.Number(label="Carbon Monoxide (ppm)", info=f"Concentration of CO (e.g., {example_values[5]})"),
#         gr.Number(label="Nitrogen Dioxide (ppm)", info=f"Concentration of NO2 (e.g., {example_values[6]})"),
#         gr.Number(label="Sulphur Dioxide (ppm)", info=f"Concentration of SO2 (e.g., {example_values[7]})"),
#         gr.Number(label="Ozone (ppm)", info=f"Concentration of O3 (e.g., {example_values[8]})"),
#         gr.Number(label="US AQI", info=f"Air Quality Index (e.g., {example_values[9]})")
#     ]

#     output_box = gr.Textbox(label="Predicted Weather Status", lines=2, placeholder="Prediction result will appear here...")
#     advice_box = gr.Textbox(label="Activities Recommendation", lines=2, placeholder="Advice based on the predicted weather status will appear here...")
#     example_button = gr.Button("Try Example")
#     predict_button = gr.Button("Predict")

#     # Define the prediction function to handle prediction and weather advice
#     def predict_pipeline(*input_values):
#         # Assume the prediction logic happens here (just using random selection for the example)
#         weather_labels = ['Light Rain', 'Moderate Drizzle', 'Light Drizzle', 'Moderate Rain', 'Overcast',
#                           'Heavy Rain', 'Dense Drizzle', 'Mainly Clear', 'Clear Sky', 'Partly Cloudy']
#         predicted_label = random.choice(weather_labels)  # Randomly choose a label for the example
#         weather_advice = get_weather_advice(predicted_label)
#         return predicted_label, weather_advice

#     predict_button.click(fn=predict_pipeline, inputs=inputs, outputs=[output_box, advice_box])
#     example_button.click(fn=set_example_values, inputs=[], outputs=inputs)

# def preload_plot():
#     """Preload default plot and advice for 3 days."""
#     fig, advice = plot_aqi(3)  # Default to 3 days
#     return fig, advice

# def update_plot_and_advice(pred_days):
    """Update plot and advice based on selected days."""
    fig, advice = plot_aqi(pred_days)
    return fig, advice

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

    # with gr.Tab("Question 3"):
    #     web_question3()

    # with gr.Tab("Question 4"):
    #     web_question4()

    # with gr.Tab("Question 5"):
    #     web_question5()

    # with gr.Tab("AQI Prediction"):
    #     with gr.Column():
    #         with gr.Row():
    #             # Slider to select number of days to predict
    #             min_days = gr.Slider(
    #                 minimum=1,
    #                 maximum=7,
    #                 value=7,
    #                 step=1,
    #                 label="Days to Predict"
    #             )

    #         btn = gr.Button(value="Update Prediction")
    #         map = gr.Plot(label="Predicted AQI Visualization")

    #     # Load plot when the page is loaded
    #     demo.load(plot_aqi, [min_days], map)

    #     # Update the plot when the button is clicked
    #     btn.click(plot_aqi, [min_days], map)

    # with gr.Tab("Weather Classifier"):
    #     classifier_tab()

gr.close_all()  # Để dừng tất cả giao diện Gradio đang chạy
demo.close()
demo.launch(share=True)

