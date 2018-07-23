[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

<h1>Network Security Manager deployment</h1>
<p>The Manager software has a Web-based user interface for configuring and managing Network Security Platform. The Network Security Manager is installed as a virtual machine in Azure environment or on-premises. All the Sensors that are deployed in the network to inspect traffic are managed by the Network Security Manager. The Manager functions are configured and managed through a GUI application, which includes complementary interfaces for alerts, system status, system configuration, report generation, and fault management. All interfaces are logically parts of the Manager program. The You can deploy the Network Security Manager using a template. You can further customize the template to suit your network requirements by downloading the json file that contains the basic template.</p>
<h2>Documentation</h2>
<p>For more information on deploying Network Security Manager in Azure, refer <a href="https://kc.mcafee.com/corporate/index?page=content&amp;id=PD27461&amp;actp=null&amp;viewlocale=en_US&amp;showDraft=false&amp;platinum_status=false&amp;locale=en_US">Network Security Platform 9.2 Virtual IPS Administration Guide</a>.</p>
<h2>Pre-requisites</h2>
<p>Following are the pre-requisites to deploy a Network Security Manager using the Azure Resource Manager (ARM) template:</p>
<ul>
<li style="text-indent: -.25in;">If the Manager is deployed behind a firewall, you must update your firewalls rules such that ports are open for Manager, Sensor, and vNSP Controller communication. For more information on the ports required for communication, see the topic <em>&ldquo;Requirements to deploy Network Security Platform in Azure environment&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
<li style="text-indent: -.25in;">An Azure subscription account is required to deploy the Network Security Manager.</li>
<li style="text-indent: -.25in;">Security groups should be created before deploying the Network Security Manager.</li>
</ul>
<p>To deploy the Network Security Manager using the template, perform the following steps:</p>
<ol>
<li style="text-indent: -.25in;">Log in to the machine which has the Azure CLI installed on it.</li>
</ol>
<p>If you are logging in to the Azure CLI for the first time, execute the following command:</p>
<p><span style="font-size: 10.0pt; line-height: 107%; font-family: 'Courier New';">az login</span></p>
<ol start="2">
<li style="text-indent: -.25in;">Execute <span style="font-size: 10.0pt; line-height: 107%; font-family: 'Courier New';">az vm image list --all -p mfe_azure --sku mcafee-vnsp-azure-nsm</span>.</li>
</ol>
<p>Note the urn generated for the Network Security Manager image.</p>
<ol start="3">
<li style="text-indent: -.25in;">Execute <span style="font-size: 10.0pt; line-height: 107%; font-family: 'Courier New';">az vm image accept-terms --urn &lt;manager_image_urn&gt;</span>.</li>
<li style="text-indent: -.25in;">Go to <a href="https://github.com/mcafee/NSP/tree/master/Azure%20Templates">McAfee Github for vNSP on Azure</a> where the vNSP component templates are available.</li>
<li style="text-indent: -.25in;">In the <strong>Github</strong> page, click <strong>McAfee NSM</strong>.</li>
<li style="text-indent: -.25in;">The <strong>McAfee NSM</strong> template page opens.</li>
<li style="text-indent: -.25in;">Click <strong>Deploy to Azure</strong>.</li>
<li style="text-indent: -.25in;">The <strong>Deploy to Azure</strong> page opens.</li>
<li style="text-indent: -.25in;">Enter the details for the Network Security Manager:</li>
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
<p style="margin-bottom: .0001pt; line-height: normal;">Select the Resource Group where the Network Security Manager should be deployed.</p>
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
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual machine name for the Network Security Manager.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Virtual Machine Size</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual machine size as <strong>Standard_D4s_v3</strong>.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Admin Username</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter a username for the Network Security Manager virtual machine.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Admin Password</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter a password for the Network Security Manager virtual machine.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Virtual Network Name</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual network name where the Network Security Manager should be deployed.</p>
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
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Subnet Name</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the subnet where the Network Security Manager should be deployed.</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>Support</h2>
<p>The Network Security Manager template is not supported by McAfee through the usual support modes which is McAfee Technical Support. The templates will be updated on a best-effort basis and any troubleshooting in case of template deployment failure will not be supported by McAfee.</p>