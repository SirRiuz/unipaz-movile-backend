

def get_future_califications(califications:list) -> (list):
    """Get a list with the future califications"""
    cal = []
    porcentajes = []
    for item in califications:
        porcentajes.append(eval(item.get(
            "porcentaje").replace("%", "/100")))

        if item.get("calification") != '--':
            cal.append(float(
                item.get("calification")))

    if len(cal) == 1:
        first_calification = cal[0]
        second_calification = 0.0
        result = 0.0

        while True:
            end_court = (((3.0 - (first_calification * porcentajes[0])) \
                - second_calification * porcentajes[1]) / porcentajes[2])
            end_court = round(end_court, 1)
            second_calification = round(second_calification, 1)
            result = (first_calification * porcentajes[0] \
                + second_calification * porcentajes[1] \
                    + end_court * porcentajes[2])

            if result == 3.0 and second_calification \
                >= 3.0 and end_court <= 5.0:
                return ({
                    "porcentaje": f"{porcentajes[0]*100}%",
                    "calification": cal[0],
                    "isBadCalification": cal[0] < 3.0
                }, {
                    "porcentaje": f"{porcentajes[1]*100}%",
                    "calification": second_calification,
                    "isBadCalification": second_calification < 3.0
                }, {
                    "porcentaje": f"{porcentajes[2]*100}%",
                    "calification": end_court,
                    "isBadCalification":end_court < 3.0})
            
            elif second_calification >= 99:
                break

            second_calification += .1

    if len(cal) == 2:
        data = []
        end_court = ((3.0 - cal[0]*porcentajes[0]) \
            - cal[1]*porcentajes[1]) / porcentajes[2]
        end_court = round(end_court, 2)

        for index in range(0, 2):
            data.append({
                "porcentaje": f"{porcentajes[index]*100}%",
                "calification": cal[index],
                "isBadCalification": cal[index] < 3.0
            })
        
        data.append({
                "porcentaje": f"{porcentajes[2]*100}%",
                "calification": end_court,
                "isBadCalification":end_court < 3.0})

        return data
