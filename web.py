from http.server import HTTPServer,BaseHTTPRequestHandler
content = """ <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>simple web server</title>
    <style>
        table{
            width: 600px;
            height: 400px;
            border: 1px solid black;
            text-align: center;
            margin-left: auto;
            margin-top: auto;
            margin-bottom: auto;
            margin-right: auto;
        }
        th,td{
            border: 1px solid black;
            padding: 10px;
            font-size: large;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            
        }
        th{
            background-color: #e5ffe1;
        }
        td{
            background-color: #d8eeff;
        }
        body{
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
</head>
<body bgcolor="fff5d4">
    <table>
        <tr>
            <th>TCP/IP MODEL</th>
            <th>TCP/IP PROTOCOL SUITE</th>
        </tr>
        <tr>
            <td style="color: crimson;">Application Layer</td>
            <td style="color: crimson;">HTTP,FTP,TFTP,DNS,DHCP,SMTP,Telnet</td>
        </tr>
        <tr>
            <td style="color: coral;">Transport Layer</td>
            <td style="color: coral;">TCP,UDP</td>
        </tr>
        <tr>
            <td style="color: darkorchid;">Internet Layer</td>
            <td style="color: darkorchid;">IP</td>
        </tr>
        <tr>
            <td style="color: midnightblue;">Network Interface Layer</td>
            <td style="color: midnightblue;">Ethernet,Token Ring,Frame Relay,ATM</td>
        </tr>
    </table>
    
</body>
</html>"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()