import convertapi

convertapi.api_secret = 'INSERT_SECRET_KEY_HERE'
result = convertapi.convert(
    'pdf',
    {
        'Url': 'https://www.instagram.com/muh.khadaffy',
        'FileName': '(Nama_File)',
    },
    from_format = 'web',
    timeout = 180,
)
tempat_file = '(Pilih Lokasi File)'
tempat_file = result.save_files(tempat_file)
print("Berhasil Mengkonversikan!\n Di simpan ke dalam [%s]" % tempat_file)