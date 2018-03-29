[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

<h1>Controller deployment</h1>
<p>The vNSP Controller is deployed as a virtual machine in Azure cloud. You can deploy the Controller in Azure cloud using the Azure CLI commands or by using the basic Controller template provided by McAfee. You can further customize the template to suit your network requirements by downloading the json file that contains the basic template.</p>
<h2>Documentation</h2>
<p>For more information on deploying vNSP solution in Azure, refer <a href="https://kc.mcafee.com/corporate/index?page=content&amp;id=PD27461&amp;actp=null&amp;viewlocale=en_US&amp;showDraft=false&amp;platinum_status=false&amp;locale=en_US">Network Security Platform 9.2 Virtual IPS Administration Guide</a>.</p>
<h2>Pre-requisites</h2>
<p>Following are the pre-requisites to deploy a vNSP Controller using the Azure Resource Manager (ARM) template:</p>
<ul>
<li>A registered application must be created to generate the application key. The application key is required for the Controller and Manager communication. With the help of the application key, the Controller retrieves information about the users from the Manager. For more information on creating a registered application, see the topic <em>&ldquo;Create a registered application&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
<li>Network Security Manager virtual machine should be deployed in Azure cloud for the Controller to establish communication with the Manager. For more information on creating a Controller in the Network Security Manager, see the topic <em>&ldquo;Configure a vNSP Controller in Azure&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
<li>Subscription, Resource Group, Virtual Network, and Subnet should be defined before deploying the Controller.</li>
<li>Make sure to add an inbound rule in the Network Security Manager virtual machine for port 443 for the Controller to successfully register with the Manager. For more information on the ports required for Controller and Manager communication, see the topic &ldquo;<em>Requirements to deploy Network Security Platform in Azure environment&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
</ul>
<h2>Deployment</h2>
<p>To deploy the vNSP Controller using the template, perform the following steps:</p>
<ol>
<li>In the Github page, click McAfee Controller.</li>
<li>The Controller template page opens.</li>
<li>Click Deploy to Azure.</li>
<li>The Deploy to Azure page opens.</li>
<li>Enter the details for the Controller:</li>
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
<p>Select the Resource Group where the Controller has to be deployed.</p>
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
<p>Enter the virtual machine name for the Controller.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Virtual Machine Size</strong></p>
</td>
<td width="420">
<p>Enter the virtual machine size as <strong>E2S_V3 Standard</strong>.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Admin Username</strong></p>
</td>
<td width="420">
<p>Enter a username for the Controller virtual machine. This should be the same name that was provided in the Network Security Manager.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Admin Password</strong></p>
</td>
<td width="420">
<p>Enter a password for the Controller virtual machine.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Custom Data</strong></p>
</td>
<td width="420">
<p>Enter the custom data for the Controller as {"Primary NSM IP":"10.x.x.x", "Controller Name":"controller_name", "Controller Shared Key":"passphrase"}. When using an MDR pair, provide the user data as {"Primary NSM IP":"10.x.x.x", "Secondary NSM IP":"10.x.x.x", "Controller Name":"controller_name", "Controller Shared Key":"passphrase"}.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Virtual Network Name</strong></p>
</td>
<td width="420">
<p>Enter the virtual network name where the Controller should be deployed.</p>
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
<p>Enter the subnet where the Controller should be deployed.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Subnet 2</strong></p>
</td>
<td width="420">
<p>&nbsp;</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>Support</h2>
<p>The Controller template is not supported by McAfee through the usual support modes as McAfee Technical Support. The templates will be updated on a best-effort basis and any troubleshooting in case of template deployed failure will not be supported by McAfee.</p>