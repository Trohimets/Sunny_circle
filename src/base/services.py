def get_path_upload_report_file(instance, file):
    """
    Построение пути к файлу, format: (media)/report_files/{report_type}/{file.pdf}
    """
    return f'report_files/{instance.reporttype_id.name}/{file}'
