from SinCity.Scanners.port_scanner import scanner

result_scanner = scanner(domain='scanme.nmap.org', min_port=5, max_port=90)
print(result_scanner)
