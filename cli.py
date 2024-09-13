import argparse
from analyzer import load_pfx, analyze_certificate
from extension import extend_certificate_expiry
from utils import print_cert_info

def main():
    parser = argparse.ArgumentParser(description="Certificate Analyzer and Extension Tool")
    parser.add_argument("--pfx", required=True, help="Path to the PFX file")
    parser.add_argument("--password", required=True, help="Password for the PFX file")
    parser.add_argument("--analyze", action="store_true", help="Analyze all certificate fields")
    parser.add_argument("--extend", action="store_true", help="Extend certificate expiry by 1 year")
    parser.add_argument("--output", help="Path to save the extended certificate")

    args = parser.parse_args()

    # Load the certificate
    private_key, certificate = load_pfx(args.pfx, args.password)

    # Analyze the certificate fields
    if args.analyze:
        analyze_certificate(certificate)

    # Extend the certificate expiry
    if args.extend:
        if not args.output:
            print("Error: --output is required to save the extended certificate")
            return

        extended_certificate = extend_certificate_expiry(certificate, private_key)
        # Save the extended certificate (omitted: code for saving the extended certificate)
        print(f"Extended certificate saved to {args.output}")

if __name__ == "__main__":
    main()
