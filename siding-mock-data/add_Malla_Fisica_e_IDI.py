import copy
import json


def load_json(file_path):
    """Load a JSON file and return its content."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
        return None


CURSOS = {
    "FIZ0411": {"Sigla": "FIZ0411", "Nombre": "Mecanica Estadistica", "Creditos": 10, "Semestralidad": "I"},
    "FIZ0412": {"Sigla": "FIZ0412", "Nombre": "Fisica Cuantica II", "Creditos": 10, "Semestralidad": "I"},
    "FIZ1426": {"Sigla": "FIZ1426", "Nombre": "Mecanica Estadistica II", "Creditos": 10, "Semestralidad": None},
}

NOMBRES = {
    "M206": "Major en Ingeniería, Diseño e Innovación (Interdisciplinario)",
    "M265": "Major en Ingeniería Física",
}

MALLAS = {
    "M206": {
        "A1": {
            "name": " Major en Ingeniería, Diseño e Innovación - Área Ingeniería Mecánica",
            "cursos": ["ICM2022", "ICM2503"],
            "lista": "CM206H44441",
        },
        "A2": {
            "name": " Major en Ingeniería, Diseño e Innovación - Área Tecnologías de la Información y Computación",
            "cursos": ["IIC2233", "IIC2143", "IIC2343", "IIC2413", "IIC2513", "IIC2026"],
            "lista": "CM206H44442",
        },
        "A3": {
            "name": " Major en Ingeniería, Diseño e Innovación - Área Ingeniería Civil",
            "cursos": [
                "ICE2313",
                "ICE2114",
                "ICC2204",
                "ICC2304",
                "ICC2105",
                "ICC2514",
                "ICT2904",
                "ICH2114",
                "ICH2304",
            ],
            "lista": "CM206H44443",
        },
        "A4": {
            "name": " Major en Ingeniería, Diseño e Innovación - Área Ingeniería Eléctrica",
            "cursos": ["IEE2103", "IEE2413", "IEE2713"],
            "lista": "CM206H44444",
        },
        "A5": {
            "name": " Major en Ingeniería, Diseño e Innovación - Área Diseño",
            "cursos": ["DNO1022", "DNO1042", "DNO1014"],
            "lista": "CM206H44445",
        },
    },
    "M265": {
        "A1": {
            "name": "Major en Ingeniería Física - Área de Ingeniería Mecánica",
            "cursos": ["ICH1104", "ICM2403", "FIZ1426", "ICM2028", "ICE2313", "ICM2213"],
            "lista": "CM265H44441",
        },
        "A2": {
            "name": "Major en Ingeniería Física - Área de Ingeniería Eléctrica",
            "cursos": ["IEE2103", "IEE2413", "IEE2613", "IEE2713", "IEE2463"],
            "lista": "CM265H44442",
        },
        "A3": {
            "name": "Major en Ingeniería Física - Área de Física",
            "cursos": ["FIZ0411", "FIZ0412"],
            "lista": "CM265H44443",
        },
    },
}


def buscar_cursos(mallas, codigo):
    cursos_buscar = set()
    for area in MALLAS[codigo]:
        cursos_buscar.update(MALLAS[codigo][area]["cursos"])

    encontrados = CURSOS.copy()
    for key in mallas["getListaPredefinida"]:
        if mallas["getListaPredefinida"][key] is None:
            continue

        for curso in mallas["getListaPredefinida"][key]:
            if curso["Sigla"] in cursos_buscar:
                encontrados[curso["Sigla"]] = curso
                cursos_buscar.remove(curso["Sigla"])

    return encontrados


def update_getListadoMajor(nueva_malla, codigo):
    for area in MALLAS[codigo]:
        nueva_malla["getListadoMajor"]["{}"].append(
            {
                "CodMajor": f"{codigo}-{area}",
                "Nombre": MALLAS[codigo][area]["name"],
                "VersionMajor": "Vs.02",
                "Curriculum": {"strings": ["C2013", "C2020", "C2022"]},
            }
        )


def update_getMajorMinorAsociado(vieja_malla, nueva_malla, codigo):
    original = vieja_malla["getMajorMinorAsociado"][f'{{"CodMajor": "{codigo}"}}']
    for area in MALLAS[codigo]:
        new_key = f'{{"CodMajor": "{codigo}-{area}"}}'
        nueva_malla["getMajorMinorAsociado"][new_key] = original.copy()


def update_getMallaSugerida(vieja_malla, nueva_malla, codigo):
    keys = []
    for malla_key in vieja_malla["getMallaSugerida"].keys():
        if json.loads(malla_key)["CodMajor"] == codigo:
            keys.append(malla_key)

    for key in keys:
        for area in MALLAS[codigo]:
            datos = copy.deepcopy(vieja_malla["getMallaSugerida"][key])
            for curso in datos:
                if curso["Programa"] == NOMBRES[codigo]:
                    curso["Programa"] = MALLAS[codigo][area]["name"]
                if curso["CodSigla"] is None and curso["CodLista"] is None:
                    curso["CodLista"] = MALLAS[codigo][area]["lista"]
                    curso["BloqueAcademico"] = "Major"
            nueva_key = key.replace(codigo, f"{codigo}-{area}")
            nueva_malla["getMallaSugerida"][nueva_key] = copy.deepcopy(datos)


def update_getListaPredefinida(vieja_malla, nueva_malla, codigo):
    cursos = buscar_cursos(vieja_malla, codigo)
    for area in MALLAS[codigo]:
        lista_curso = []
        for curso in MALLAS[codigo][area]["cursos"]:
            lista_curso.append(cursos[curso])
        new_key = f'{{"CodLista": "{MALLAS[codigo][area]["lista"]}"}}'
        nueva_malla["getListaPredefinida"][new_key] = lista_curso


if __name__ == "__main__":
    malla_actual = load_json("mallas.json")
    nueva_malla = {key: {} for key in malla_actual}
    nueva_malla["getListadoMajor"]["{}"] = []
    for codigo in MALLAS:
        update_getListadoMajor(nueva_malla, codigo)
        update_getMajorMinorAsociado(malla_actual, nueva_malla, codigo)
        update_getMallaSugerida(malla_actual, nueva_malla, codigo)
        update_getListaPredefinida(malla_actual, nueva_malla, codigo)

    with open("mallas_nuevas.json", "w", encoding="utf-8") as file:
        json.dump(nueva_malla, file, indent=4, ensure_ascii=False)
