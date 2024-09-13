from cryptography import x509
import datetime

def extend_certificate_expiry(certificate, private_key, extra_days=365):
    """ Extend the certificate's expiry date by the given number of days. """
    new_valid_to = certificate.not_valid_after + datetime.timedelta(days=extra_days)

    # Build a new certificate
    extended_certificate = x509.CertificateBuilder().subject_name(
        certificate.subject
    ).issuer_name(
        certificate.issuer
    ).public_key(
        certificate.public_key()
    ).serial_number(
        certificate.serial_number
    ).not_valid_before(
        certificate.not_valid_before
    ).not_valid_after(
        new_valid_to
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"")]),
        critical=False,
    ).sign(private_key, certificate.signature_hash_algorithm)

    return extended_certificate
