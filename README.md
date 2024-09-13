# Certificate Analyzer and Extension Tool
A tool for the analysis, validation, and extension of SSL/TLS certificates.
This tool is designed to help developers, security professionals, and system administrators to inspect and manipulate PFX (PKCS#12) certificate files. Whether you need to print detailed certificate fields or extend the validity of an expired certificate, this tool simplifies the process.

## Features

- **Analyze PFX Certificates**: Load PFX (PKCS#12) files and display all certificate fields including subject, issuer, serial number, validity period, and extensions.
- **Detailed Field Inspection**: Print detailed information about all certificate fields such as key usage, public key algorithm, and more.
- **Extend Expiry Dates**: Automatically extend the expiry date of certificates by 1 year while maintaining all existing fields and properties.

## Installation

To get started, follow these steps to set up the tool locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Zero-Defense-Labs/certificate-analyzer.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd certificate-analyzer
    ```
3. **Install dependencies**:
    Ensure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```


## Usage

This tool provides two functionalities: certificate analysis and expiry extension. 

### 1. Analyze Certificate Fields

To analyze and print all fields from a PFX certificate, use the `--analyze` flag. This will display certificate details such as subject, issuer, validity dates, and extensions.

```bash
python3 cli.py --pfx <path_to_pfx> --password <password> --analyze
```

#### Example:
```bash
python3 cli.py --pfx certs/mycert.pfx --password mypassword --analyze
```

#### Sample Output:
```
==== Certificate Details ====
Subject       : <Name(C=US,O=Example,CN=example.com)>
Issuer        : <Name(C=US,O=Example CA,CN=Example Root CA)>
Serial Number : 1234567890
Valid From    : 2023-01-01 00:00:00
Valid To      : 2024-01-01 00:00:00
Version       : v3
Public Key Algorithm: sha256WithRSAEncryption

Extensions:
- basicConstraints: CA:FALSE
- keyUsage: Digital Signature, Key Encipherment
- subjectAltName: example.com
```

### 2. Extend Certificate Expiry

To extend the expiry of a certificate by 1 year, use the `--extend` flag along with an output path to save the modified PFX file. The certificate will retain all its original fields and properties, but the validity period will be extended.

```bash
python3 cli.py --pfx <path_to_pfx> --password <password> --extend --output <output_pfx> --new_password <new_password>
```

#### Example:
```bash
python3 cli.py --pfx certs/mycert.pfx --password mypassword --extend --output certs/extended_cert.pfx --new_password newpassword
```

This will extend the certificate expiry by 1 year and save the updated certificate to `extended_cert.pfx`.

### Command-Line Options
| Option        | Description                                                                 |
| ------------- | --------------------------------------------------------------------------- |
| `--pfx`       | Path to the PFX certificate file.                                            |
| `--password`  | Password for the PFX file.                                                   |
| `--analyze`   | Print detailed fields of the certificate.                                    |
| `--extend`    | Extend the expiry of the certificate by 1 year.                              |
| `--output`    | (Required with `--extend`) Path to save the extended PFX certificate.        |
| `--new_password` | (Required with `--extend`) Password for the new PFX file.                    |


## Contributing

We welcome contributions to improve and extend the functionality of this tool. To contribute:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Make your changes and write tests if applicable.
4. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

If you encounter any issues or have questions, feel free to open an issue on GitHub or reach out via email at [jacob@zero-defense.com](mailto:jacob@zero-defense.com).

