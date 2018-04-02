[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

<h1>Virtual IPS Sensor deployment with double interface</h1>
<p>The Virtual IPS Sensors are high-performance, scalable, and flexible content processing appliances built for accurate detection and prevention of intrusions. Virtual IPS Sensors are deployed as a virtual machine in Azure cloud. You can deploy the Sensor in Azure cloud using the Azure CLI commands or by using the basic Sensor template provided by McAfee. The Virtual IPS Sensors can be deployed with single interface or double interface. In a single interface Sensor deployment, both management traffic and data traffic uses a single interface. In a double interface Sensor deployment, the management traffic uses one interface and the data traffic uses another interface for traffic flow. You can further customize the template to suit your network requirements by downloading the json file that contains the basic template. The following template deploys the Virtual IPS Sensor with a double interface.</p>
<h2>Documentation</h2>
<p>For more information on deploying vNSP solution in Azure, refer <a href="https://kc.mcafee.com/corporate/index?page=content&amp;id=PD27461&amp;actp=null&amp;viewlocale=en_US&amp;showDraft=false&amp;platinum_status=false&amp;locale=en_US">Network Security Platform 9.2 Virtual IPS Administration Guide</a>.</p>
<h2>Pre-requisites</h2>
<p>Following are the pre-requisites to deploy a Virtual IPS Sensor with double interface using the Azure Resource Manager (ARM) template:</p>
<ul>
<li>vNSP Cluster should be created in the Network Security Manager where the Virtual IPS Sensor will be deployed. For more information on creating a vNSP Cluster in the Network Security Manager, see the topic <em>&ldquo;Create a vNSP Cluster for Azure&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
<li>Subscription, Resource Group, Virtual Network, and Subnet along with the Network Security Group should be defined before deploying the Virtual IPS Sensor.</li>
<li>Make sure to open the ports required for Virtual IPS Sensor to communicate with the Network Security Manager. For more information on the ports required for Sensor and Manager communication, see the topic &ldquo;<em>Requirements to deploy Network Security Platform in Azure environment&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
</ul>
<h2>Deployment</h2>
<p>To deploy the Virtual IPS Sensor with a double interface using the template, perform the following steps:</p>
<ol>
<li>In the <strong>Github</strong> page, click <strong>McAfee IPS Sensor Single Interface</strong>.</li>
<li>The <strong>McAfee IPS Sensor Single Interface</strong> template page opens.</li>
<li>Click <strong>Deploy to Azure</strong>.</li>
<li>The <strong>Deploy to Azure</strong> page opens.</li>
<li>Enter the details for the Virtual IPS Sensor:</li>
</ol>
<table>
<tbody>
<tr>
<td width="204">
<p><strong>Options</strong></p>
</td>
<td width="420">
<p><strong>Definition</strong></p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Directory</strong></p>
</td>
<td width="420">
<p>Select the directory for your account.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Subscription</strong></p>
</td>
<td width="420">
<p>Select the subscription for your account.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Resource Group</strong></p>
</td>
<td width="420">
<p>Select the Resource Group where the Virtual IPS Sensor should be deployed.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Resource Group Name</strong></p>
</td>
<td width="420">
<p>Enter the Resource Group Name.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Virtual Machine Name</strong></p>
</td>
<td width="420">
<p>Enter the virtual machine name for the Virtual IPS Sensor.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Virtual Machine Size</strong></p>
</td>
<td width="420">
<p>Enter the virtual machine size as <strong>F8S Standard</strong>.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Admin Username</strong></p>
</td>
<td width="420">
<p>Enter a username for the Virtual IPS Sensor virtual machine.</p>
<p><strong>Note:</strong> The Virtual IPS Sensor name should not exceed 25 characters.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Admin Password</strong></p>
</td>
<td width="420">
<p>Enter a password for the Virtual IPS Sensor virtual machine.</p>
<p><strong>Note:</strong> Only password authentication type is supported for Sensors.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Custom Data</strong></p>
</td>
<td width="420">
<p>Enter the custom data for the Virtual IPS Sensor as {"Primary NSM IP":"10.x.x.x", "Cluster Name":"Cluster_Name", "Sensor Shared Key":"passphrase", "dataSubnet":"subnet2"}. When using an MDR pair, provide the user data as {"Primary NSM IP":"10.x.x.x", "Secondary NSM IP":"10.x.x.x", "Cluster Name":"Cluster_Name", "Sensor Shared Key":"passphrase", "dataSubnet":"subnet2"}.</p>
<p>&nbsp;</p>
<table>
<tbody>
<tr>
<td width="155">
<p>Primary NSM IP</p>
</td>
<td width="250">
<p>IP address of the primary Manager</p>
</td>
</tr>
<tr>
<td width="155">
<p>Secondary NSM IP</p>
</td>
<td width="250">
<p>IP address of the secondary Manager</p>
</td>
</tr>
<tr>
<td width="155">
<p>Cluster Name</p>
</td>
<td width="250">
<p>Name of the Cluster in the Manager where the auto scale group will be launched</p>
</td>
</tr>
<tr>
<td width="155">
<p>Sensor Shared Key</p>
</td>
<td width="250">
<p>Shared secret key to establish trust with the Sensor</p>
</td>
</tr>
<tr>
<td width="155">
<p>dataSubnet</p>
</td>
<td width="250">
<p>Second subnet which the Sensor uses for monitoring traffic</p>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Virtual Network Name</strong></p>
</td>
<td width="420">
<p>Enter the virtual network name where the Virtual IPS Sensor should be deployed.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Virtual Network Resource Group Name</strong></p>
</td>
<td width="420">
<p>Enter the virtual network resource group name.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Subnet 1</strong></p>
</td>
<td width="420">
<p>Enter the subnet which is used by the Virtual IPS Sensor for management traffic and to communicate with the Network Security Manager.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Subnet 2</strong></p>
</td>
<td width="420">
<p>Enter the subnet which is used by the Virtual IPS Sensor for data traffic which should be inspected by the Sensor.</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>Support</h2>
<p>The Virtual IPS Sensor template is not supported by McAfee through the usual support modes which is McAfee Technical Support. The templates will be updated on a best-effort basis and any troubleshooting in case of template deployment failure will not be supported by McAfee.</p>