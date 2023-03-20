from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


RECITATION_HOURS = {"a": "09:00~09:50", "b": "10:00~10:50",
                    "c": "11:00~11:50", "d": "12:00~12:50"}
MICROSERVICE_LINK = "https://whos-my-ta.fly.dev/section_id/"


@app.get("/section_info/{section_id}")
def get_section_info(section_id: str):

    if section_id is None:
        raise HTTPException(status_code=404, detail="Missing section id")

    section_id = section_id.lower()

    response = requests.get("https://whos-my-ta.fly.dev/section_id/" + section_id)

    # You can check out what the response body looks like in terminal using the print statement
    data = response.json()
    print(data)
    ta_name_list = data["ta_names"]
    ta1_name = ta_name_list[0]["fname"] + " " + ta_name_list[0]["lname"]
    ta2_name = ta_name_list[1]["fname"] + " " + ta_name_list[1]["lname"]

    print(ta1_name)

    hr = ""
    if section_id == "a": hr = "09"
    elif section_id == "b": hr = "10"
    elif section_id == "c": hr = "11"
    else: hr = "12"

    # TODO
    if section_id == "a":
        return {
            "section": section_id.upper(),
            "start_time": hr + ":00"
            "end_time": hr + ":50",
            "ta": [ta1_name, ta2_name]
        }
    else:
        raise HTTPException(status_code=404, detail="Invalid section id")
