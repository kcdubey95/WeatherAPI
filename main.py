from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api import weather_api

app = FastAPI()


@app.get("/{location}", response_class=HTMLResponse)
async def read_items(location: str):
    try:
        data = await weather_api(location)

        city = data['location']['name']
        wind_speed = f"{data['current']['wind_kph']} kph"
        temperature = data['current']['temp_c']
        icon = data['current']['condition']['icon']
        pro_pos = data['current']['precip_mm']
        sun = data['current']['uv']
        current_time = datetime.now().strftime("%H:%M")
        html_content = f"""
        <html>
            <head>
                <title>Weather</title>
                <!-- Font Awesome -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/7.3.2/mdb.min.css"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <script
                  type="text/javascript"
                  src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/7.3.2/mdb.umd.min.js"
                ></script>
            </head>
            <body>
                <div class="row d-flex justify-content-center py-5 bg-secondary">
                    <div class="col-md-8 col-lg-6 col-xl-5">
                        <div class="card text-body" style=" border-radius: 35px;">
                            <div class="card-body p-4">
                                <div class="d-flex">
                                    <h6 class="flex-grow-1">{city}</h6>
                                     <h6>{current_time}</h6>
                                </div>
                                <div class="d-flex flex-column text-center mt-5 mb-4">
                                    <h6 class="display-4 mb-0 font-weight-bold"> {temperature}°C </h6>
                                    <span class="small" style="color: #868B94">Stormy</span>
                                </div>
                                <div class="d-flex align-items-center">
                                    <div class="flex-grow-1" style="font-size: 1rem;">
                                        <div><i class="fas fa-wind fa-fw" style="color: #868B94;"></i> <span class="ms-1"> {wind_speed}
                                          </span>
                                        </div>
                                        <div><i class="fas fa-tint fa-fw" style="color: #868B94;"></i> <span class="ms-1"> {pro_pos}%
                                          </span></div>
                                        <div><i class="fas fa-sun fa-fw" style="color: #868B94;"></i> <span class="ms-1"> {sun}
                                          </span></div>
                                    </div>
                                    <div>
                                        <img src="{icon}" width="100px">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        """

        return HTMLResponse(content=html_content, status_code=200)
    except:
        print("error")

# Note: No need to call read_items() here. FastAPI will handle it.
