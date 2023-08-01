import os

def is_file_path_exists(filePath):
    '''
    Metoda koja vraća True ili False, ovisno o tome postoji li filePath
    '''
    return os.path.exists(filePath)

def open_file_path_for_reading(filePath):
    '''
    Metoda za otvaranje konekcije prema datoteci navedenoj u filePath varijabli
    Konekcija će biti otvorena za čitanje
    '''
    if not is_file_path_exists(filePath):
        return f'Datoteka {filePath} ne postoji!'
    
    try:
        file_reader = open(filePath, 'r')
        return file_reader
    except Exception:
        return f'Dogodila se greška prilikom pokušaja otvaranja datoteke!'

def open_file_path_for_writing(file_path):
    '''
    Metoda za otvaranje konekcije prema datoteci navedenoj u filePath varijabli
    Konekcija će biti otvorena za pisanje
    '''

    try:
        file_writer = open(file_path, 'w')
        return file_writer
    except Exception:
        return f'Dogodila se greška prilikom pokušaja otvaranja datoteke!'

def close_file_connection(file_connection):
    '''
    Metoda za zatvaranje konekcije prema datoteci
    '''
    file_connection.close()

def write_to_file_path_open_close(file_path, content):
    '''
    Metoda za pisanje u datoteku
    Sadrzaj se nalazi unutar varijable content
    '''
    try:
        with open(file_path, 'w') as file_writer:
            file_writer.write(content)
    except Exception as e:
        return f'Dogodila se greška prilikom pokušaja pisanja u datoteku'

def append_to_file_path_open_close(file_path, content):
    '''
    Metoda za pisanje u datoteku
    Sadrzaj se nalazi unutar varijable content
    '''
    try:
        with open(file_path, 'a') as file_writer:
            file_writer.write(content)
    except Exception as e:
        return f'Dogodila se greška prilikom pokušaja pisanja u datoteku'
    
def read_from_file_path_open_close(file_path):
    '''
    Metoda za čitanje iz datoteke
    '''
    if not is_file_path_exists(file_path):
        return f'Datoteka {file_path} ne postoji!'
    
    try:
        with open(file_path, 'r') as file_reader:
            return file_reader.read()
        
    except Exception as e:
        return f'Dogodila se greška prilikom pokušaja čitajna iz datoteke'
    
def write_line_with_file_writer(line_writer, line_content):
    '''
    Metoda za pisanje linije pomoću konekciju u line_writer-u
    '''
    try:
        line_content = line_content + '\n'
        line_writer.write(line_content)
    
    except Exception as e:
        return f'Dogodila se greška prilikom pokušaja pisanja u datoteku'