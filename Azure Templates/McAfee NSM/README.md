[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

<h1>Network Security Manager deployment</h1>
<p>The Manager software has a Web-based user interface for configuring and managing Network Security Platform. The Network Security Manager is installed as a virtual machine in Azure environment or on-premises. All the Sensors that are deployed in the network to inspect traffic are managed by the Network Security Manager. The Manager functions are configured and managed through a GUI application, which includes complementary interfaces for alerts, system status, system configuration, report generation, and fault management. All interfaces are logically parts of the Manager program. The You can deploy the Network Security Manager using a template. You can further customize the template to suit your network requirements by downloading the json file that contains the basic template.</p>
<h2>Documentation</h2>
<p>For more information on deploying Network Security Manager in Azure, refer <a href="https://kc.mcafee.com/corporate/index?page=content&amp;id=PD27461&amp;actp=null&amp;viewlocale=en_US&amp;showDraft=false&amp;platinum_status=false&amp;locale=en_US">Network Security Platform 9.2 Virtual IPS Administration Guide</a>.</p>
<h2>Pre-requisites</h2>
<p>Following are the pre-requisites to deploy a Network Security Manager using the Azure Resource Manager (ARM) template:</p>
<ul>
<li>If the Manager is deployed behind a firewall, you must update your firewalls rules such that ports are open for Manager, Sensor, and vNSP Controller communication. For more information on the ports required for communication, see the topic <em>&ldquo;Requirements to deploy Network Security Platform in Azure environment&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
<li>An Azure subscription account is required to deploy the Network Security Manager.</li>
<li>Security groups should be created before deploying the Network Security Manager.</li>
</ul>
<p>To deploy the Network Security Manager using the template, perform the following steps:</p>
<ol>
<li>Log in to the machine which has the Azure CLI installed on it.</li>
</ol>
<p>If you are logging in to the Azure CLI for the first time, execute the following command:</p>
<p>az login</p>
<ol start="2">
<li>Execute az vm image list --all -p mfe_azure --sku mcafee-vnsp-azure-nsm.</li>
</ol>
<p>Note the urn generated for the Network Security Manager image.</p>
<ol start="3">
<li>Execute az vm image accept-terms --urn &lt;manager_image_urn&gt;.</li>
<li>Go to <a href="https://github.com/mcafee/NSP/tree/master/Azure%20Templates">McAfee Github for vNSP on Azure</a> where the vNSP component templates are available.</li>
<li>In the <strong>Github</strong> page, click <strong>McAfee NSM</strong>.</li>
<li>The <strong>McAfee NSM</strong> template page opens.</li>
<li>Click <strong>Deploy to Azure</strong>.</li>
<li>The <strong>Deploy to Azure</strong> page opens.</li>
<li>Enter the details for the Network Security Manager:</li>
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
<p>Select the Resource Group where the Network Security Manager should be deployed.</p>
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
<p>Enter the virtual machine name for the Network Security Manager.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Virtual Machine Size</strong></p>
</td>
<td width="420">
<p>Enter the virtual machine size as <strong>D4S_V3 Standard</strong>.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Admin Username</strong></p>
</td>
<td width="420">
<p>Enter a username for the Network Security Manager virtual machine.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Admin Password</strong></p>
</td>
<td width="420">
<p>Enter a password for the Network Security Manager virtual machine.</p>
</td>
</tr>
<tr>
<td width="204">
<p><strong>Virtual Network Name</strong></p>
</td>
<td width="420">
<p>Enter the virtual network name where the Network Security Manager should be deployed.</p>
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
<p><strong>Subnet Name</strong></p>
</td>
<td width="420">
<p>Enter the subnet where the Network Security Manager should be deployed.</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>Support</h2>
<p>The Network Security Manager template is not supported by McAfee through the usual support modes which is McAfee Technical Support. The templates will be updated on a best-effort basis and any troubleshooting in case of template deployment failure will not be supported by McAfee.</p>
