1.IP Address (Internet Protocol Address):-
An IP address is a unique address assigned to a device on a network so that devices can communicate
with each other.

2.DNS (Domain Name System):-
DNS converts domain names into IP addresses.

3.Port:-
A port identifies a specific service running on a device.

4.Protocol:-
A protocol is a set of rules that devices follow to communicate.
Just like humans use languages (English, Hindi), computers use protocols.

--------------------------------------------------------------------------------------------------------


How a Browser Loads a Website:-
When you enter a website URL (for example, https://www.google.com) into a browser and press Enter,
several steps occur behind the scenes before the webpage appears on your screen.

1. URL Processing:-
The browser first examines the URL to determine the protocol,the domain name,the path to the requested resource.

2. DNS Lookup:-
The browser needs the website's IP address to communicate with the server DNS translates the domain name into an IP address.

3. Establishing a Connection:-
Using the IP address, the browser connects to the web server.A TCP connection is established.
For HTTPS, a TLS/SSL handshake occurs to create a secure encrypted connection.

4. Sending the HTTP Request:-
The browser sends an HTTP request containing
Request method,URL path,headers.

5. Receiving the HTTP Response:-
The server processes the request and returns an HTTP response containing HTML, CSS, JavaScript, and other resources.

6. Parsing HTML:-
The browser begins reading the HTML document and creates the DOM (Document Object Model), which represents the webpage structure.

7. Painting and Java Script Execution:-
CSS is applied, JavaScript is executed, and the page is rendered on the screen.

8. Page Becomes Interactive:-
After rendering and JavaScript execution, the webpage is fully loaded and ready for user interaction.