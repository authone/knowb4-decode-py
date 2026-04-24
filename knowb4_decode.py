'''
    @author: George Gugulea
    @author_email: george.gugulea@certsign.ro
    @date: 2026.04.20
    @description: Parse knowb4 egress links found in emails and extract the original URL
'''
import base64
import gzip
import io
import zlib
from urllib.parse import urlsplit, unquote
from logger import Logger

def zlib_decompress_no_crc(data):
    decompressor = zlib.decompressobj(wbits=zlib.MAX_WBITS | 32)
    str_result = ""
    try:
        str_result = decompressor.decompress(data) + decompressor.flush()
    except zlib.error as e:
        Logger.LogError(f"Zlib decompression error: {e}")
        str_result = decompressor.unused_data
    return str_result

def gzip_decompress_raw_data(data):
    gzip_prefix = bytes.fromhex('1f8b 0800 0000 0000')
    # gzip_prefix = bytes.fromhex('1f8b 08')
    #zip_prefix = bytes.fromhex('1f8b 0800 6617 e969')
    gzip_data = gzip_prefix + data

    original_url = gzip.decompress(gzip_data)
    return original_url

def bytes_print_excaped(data):
    hexstringesc = ''.join(f'\\x{byte:02x}' for byte in data)
    print(hexstringesc)

def bytes_writeout(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

class KnowB4Decode:
    def __init__(self, options):
        self.options = options
        self.schema = None
        self.domain = None
        self.urlEncoded = options.url.strip()
        self.urlDecoded = None

    def decode(self):
        if not self.urlEncoded or self.urlEncoded == "":
            Logger.LogError("URL is not specified")
            return False

        urlsplited = urlsplit(self.urlEncoded)
        self.schema = urlsplited.scheme
        self.domain = urlsplited.netloc
            
        start = urlsplited.query.find("Base64Url=")
        end = urlsplited.query.find("@OriginalLink", start)
        
        if start == -1 or end == -1:
            Logger.LogError("Encoded URL is not a valid knowb4 URL")
            return False
        
        base64_url = urlsplited.query[start + len("Base64Url="):end-1]
        base64_url = unquote(base64_url).replace("_", "/").replace("-","+")
        # print(base64_url)

        original_url_zipped = base64.b64decode(base64_url, validate=True)
        # bytes_print_excaped(original_url_zipped)
        # bytes_writeout(original_url_zipped, "original_url_zipped.bin")


        self.urlDecoded = zlib_decompress_no_crc(original_url_zipped)
        # urlDecoded = gzip_decompress_raw_data(original_url_zipped)

        self.urlDecoded = self.urlDecoded.decode("utf-8", errors="replace")
        return True


    def AnalyzeURL(url):
        urlsplited = urlsplit(url)
        schema = urlsplited.scheme
        domain = urlsplited.netloc
        query = urlsplited.query
        if schema != "https":
            Logger.LogWarning("Decoded URL is not using HTTPS schema") 

# printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" |cat - application.bin.zip |gzip -dc