<p style="text-align: justify;">This template deploys McAfee vNSP Controller.</p>

[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

<p style="text-align: justify;">vNSP Controller is the central enforcement point for all network and security policies. It is a centralized manager that controls all Virtual Probes installed on the instances in the cloud environment. It can be configured in the Network Security Manager.</p>
<ul style="list-style-type: circle;">
<li style="text-align: justify;">vNSP Cluster &mdash; is a collection of Virtual IPS Sensors that inspect traffic directed to them by the virtual<br />machines.</li>
<li style="text-align: justify;">Protected group &mdash; is a collection of virtual machines that redirect their traffic to a vNSP Cluster for inspection.</li>
</ul>
<p style="text-align: justify;"><br />McAfee Virtual Probes are installed on all instances that need to be secured by the Virtual IPS Sensor. The&nbsp;Virtual Probe intercepts all traffic before it reaches its destination and then forwards it to the Virtual IPS Sensor for scanning.</p>