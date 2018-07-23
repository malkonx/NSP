[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

<h1>Virtual IPS Sensor deployment as VM scale sets with single interface</h1>
<p>The Virtual IPS Sensors are high-performance, scalable, and flexible content processing appliances built for accurate detection and prevention of intrusions. To provide high availability for Sensors in Azure cloud, you can deploy the Sensors in a VM scale set. Depending on the threshold set for parameters, the Sensors are either scaled out or scaled in. For example, if you have set a threshold for CPU utilization, depending on the CPU utilization the Sensors are scaled out in case of high CPU utilization and scaled in for low CPU utilization. When there is a Sensor virtual machine failure, a new Sensor is deployed in its place to manage the traffic. You can deploy the Sensor in Azure cloud using the Azure CLI commands or by using the basic Sensor template provided by McAfee. You can further customize the template to suit your network requirements by downloading the json file that contains the basic template. The following template deploys the Virtual IPS Sensor as a VM scale set with a single interface.</p>
<h2>Documentation</h2>
<p>For more information on deploying vNSP solution in Azure, refer <a href="https://kc.mcafee.com/corporate/index?page=content&amp;id=PD27461&amp;actp=null&amp;viewlocale=en_US&amp;showDraft=false&amp;platinum_status=false&amp;locale=en_US">Network Security Platform 9.2 Virtual IPS Administration Guide</a>.</p>
<h2>Pre-requisites</h2>
<p>Following are the pre-requisites to deploy a Virtual IPS Sensor as a VM scale set with a single interface using the Azure Resource Manager (ARM) template:</p>
<ul>
<li style="text-indent: -.25in;">vNSP Cluster should be created in the Network Security Manager where the Virtual IPS Sensor will be deployed. For more information on creating a vNSP Cluster in the Network Security Manager, see the topic <em>&ldquo;Create a vNSP Cluster for Azure&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
<li style="text-indent: -.25in;">Subscription, Resource Group, Virtual Network, and Subnet along with the Network Security Group should be defined before deploying the Virtual IPS Sensor.</li>
<li style="text-indent: -.25in;">Make sure to open the ports required for Virtual IPS Sensor to communicate with the Network Security Manager. For more information on the ports required for Sensor and Manager communication, see the topic &ldquo;<em>Requirements to deploy Network Security Platform in Azure environment&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
</ul>
<h2>Deployment</h2>
<p>To deploy the Virtual IPS Sensor as a VM scale set with a single interface using the template, perform the following steps:</p>
<ol>
<li style="text-indent: -.25in;">Log in to the machine which has the Azure CLI installed on it.</li>
</ol>
<p>If you are logging in to the Azure CLI for the first time, execute the following command:</p>
<p><span style="font-size: 10.0pt; line-height: 107%; font-family: 'Courier New';">az login</span></p>
<ol start="2">
<li style="text-indent: -.25in;">Execute <span style="font-size: 10.0pt; line-height: 107%; font-family: 'Courier New';">az vm image list --all -p mfe_azure --sku mcafee-vnsp-azure-ips-sensor-byol</span>.</li>
</ol>
<p>Note the urn generated for the Virtual IPS Sensor image.</p>
<ol start="3">
<li style="text-indent: -.25in;">Execute <span style="font-size: 10.0pt; line-height: 107%; font-family: 'Courier New';">az vm image accept-terms --urn &lt;sensor_image_urn&gt;</span>.</li>
<li style="text-indent: -.25in;">Go to <a href="https://github.com/mcafee/NSP/tree/master/Azure%20Templates">McAfee Github for vNSP on Azure</a> where the vNSP component templates are available.</li>
<li style="text-indent: -.25in;">In the <strong>Github</strong> page, click <strong>McAfee IPS Sensor Single Interface</strong>.</li>
<li style="text-indent: -.25in;">The <strong>McAfee IPS Sensor Single Interface</strong> template page opens.</li>
<li style="text-indent: -.25in;">Click <strong>Deploy to Azure</strong>.</li>
<li style="text-indent: -.25in;">The <strong>Deploy to Azure</strong> page opens.</li>
<li style="text-indent: -.25in;">Enter the details for the Virtual IPS Sensor:</li>
</ol>
<table style="border-collapse: collapse; border: none;">
<tbody>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; background: #D9D9D9; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Options</strong></p>
</td>
<td style="width: 314.75pt; border: solid windowtext 1.0pt; border-left: none; background: #D9D9D9; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Definition</strong></p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Directory</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Select the directory for your account.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Subscription</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Select the subscription for your account.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Resource Group</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Select the Resource Group where the Virtual IPS Sensor should be deployed.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Resource Group Name</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the Resource Group Name.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Virtual Machine Name</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual machine name for the Virtual IPS Sensor.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Virtual Machine Size</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual machine size as <strong>Standard_F8s</strong>.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Admin Username</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter a username for the Virtual IPS Sensor virtual machine.</p>
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Note:</strong> The Virtual IPS Sensor name should not exceed 25 characters.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Admin Password</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter a password for the Virtual IPS Sensor virtual machine.</p>
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Note:</strong> Only password authentication type is supported for Sensors.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Custom Data</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the custom data for the Virtual IPS Sensor as<span style="font-size: 9.0pt; font-family: 'Courier New';"> {"Primary NSM IP":"10.x.x.x", "Cluster Name":"Cluster_Name", "Sensor Shared Key":"passphrase", "dataSubnet":"subnet2"}. </span>When using an MDR pair, provide the user data as <span style="font-size: 9.0pt; font-family: 'Courier New';">{"Primary NSM IP":"10.x.x.x", "Secondary NSM IP":"10.x.x.x", "Cluster Name":"Cluster_Name", "Sensor Shared Key":"passphrase", "dataSubnet":"subnet2"}.</span></p>
<p style="margin-bottom: .0001pt; line-height: normal;"><span style="font-size: 9.0pt; font-family: 'Courier New';">&nbsp;</span></p>
<table style="border-collapse: collapse; border: none;">
<tbody>
<tr>
<td style="width: 116.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="155">
<p style="margin-bottom: .0001pt; line-height: normal;"><span style="font-size: 9.0pt; font-family: 'Courier New';">Primary NSM IP</span></p>
</td>
<td style="width: 187.45pt; padding: 0in 5.4pt 0in 5.4pt;" width="250">
<p style="margin-bottom: .0001pt; line-height: normal;">IP address of the primary Manager</p>
</td>
</tr>
<tr>
<td style="width: 116.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="155">
<p style="margin-bottom: .0001pt; line-height: normal;"><span style="font-size: 9.0pt; font-family: 'Courier New';">Secondary NSM IP</span></p>
</td>
<td style="width: 187.45pt; padding: 0in 5.4pt 0in 5.4pt;" width="250">
<p style="margin-bottom: .0001pt; line-height: normal;">IP address of the secondary Manager</p>
</td>
</tr>
<tr>
<td style="width: 116.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="155">
<p style="margin-bottom: .0001pt; line-height: normal;"><span style="font-size: 9.0pt; font-family: 'Courier New';">Cluster Name</span></p>
</td>
<td style="width: 187.45pt; padding: 0in 5.4pt 0in 5.4pt;" width="250">
<p style="margin-bottom: .0001pt; line-height: normal;">Name of the Cluster in the Manager where the auto scale group will be launched</p>
</td>
</tr>
<tr>
<td style="width: 116.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="155">
<p style="margin-bottom: .0001pt; line-height: normal;"><span style="font-size: 9.0pt; font-family: 'Courier New';">Sensor Shared Key</span></p>
</td>
<td style="width: 187.45pt; padding: 0in 5.4pt 0in 5.4pt;" width="250">
<p style="margin-bottom: .0001pt; line-height: normal;">Shared secret key to establish trust with the Sensor</p>
</td>
</tr>
<tr>
<td style="width: 116.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="155">
<p style="margin-bottom: .0001pt; line-height: normal;"><span style="font-size: 9.0pt; font-family: 'Courier New';">dataSubnet</span></p>
</td>
<td style="width: 187.45pt; padding: 0in 5.4pt 0in 5.4pt;" width="250">
<p style="margin-bottom: .0001pt; line-height: normal;">Second subnet which the Sensor uses for monitoring traffic</p>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Virtual Network Name</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual network name where the Virtual IPS Sensor should be deployed.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Virtual Network Resource Group Name</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual network resource group name.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Subnet 1</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the subnet which is used by the Virtual IPS Sensor for management traffic and to communicate with the Network Security Manager.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Subnet 2</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the subnet which is used by the Virtual IPS Sensor for data traffic which should be inspected by the Sensor.</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>Support</h2>
<p>The Virtual IPS Sensor template is not supported by McAfee through the usual support modes which is McAfee Technical Support. The templates will be updated on a best-effort basis and any troubleshooting in case of template deployment failure will not be supported by McAfee.</p>
<p>&nbsp;</p>