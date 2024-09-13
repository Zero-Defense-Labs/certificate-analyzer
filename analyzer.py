from cryptography import x509
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509.oid import NameOID
from utils import print_cert_info

def load_pfx(pfx_file, password):
    with open(pfx_file, "rb") as file:
        pfx_data = file.read()
    
    private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(
        pfx_data, password.encode()
    )
    return private_key, certificate

def analyze_certificate(certificate):
    """ Analyze and print all fields of the given certificate. """
    print_cert_info("Subject", certificate.subject)
    print_cert_info("Issuer", certificate.issuer)
    print_cert_info("Serial Number", certificate.serial_number)
    print_cert_info("Valid From", certificate.not_valid_before)
    print_cert_info("Valid To", certificate.not_valid_after)

    # Additional fields
    print_cert_info("Version", certificate.version)
    print_cert_info("Public Key Algorithm", certificate.signature_algorithm_oid._name)

    # Extensions
    print("\nExtensions:")
    for ext in certificate.extensions:
        print(f"- {ext.oid._name}: {ext.value}")
