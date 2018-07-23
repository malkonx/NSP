[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

<h1>Controller deployment</h1>
<p>The vNSP Controller is deployed as a virtual machine in Azure cloud. You can deploy the Controller in Azure cloud using the Azure CLI commands or by using the basic Controller template provided by McAfee. You can further customize the template to suit your network requirements by downloading the json file that contains the basic template.</p>
<h2>Documentation</h2>
<p>For more information on deploying vNSP solution in Azure, refer <a href="https://kc.mcafee.com/corporate/index?page=content&amp;id=PD27461&amp;actp=null&amp;viewlocale=en_US&amp;showDraft=false&amp;platinum_status=false&amp;locale=en_US">Network Security Platform 9.2 Virtual IPS Administration Guide</a>.</p>
<h2>Pre-requisites</h2>
<p>Following are the pre-requisites to deploy a vNSP Controller using the Azure Resource Manager (ARM) template:</p>
<ul>
<li style="text-indent: -.25in;">A registered application must be created to generate the application key. The application key is required for the Controller and Manager communication. With the help of the application key, the Controller retrieves information about the users from the Manager. For more information on creating a registered application, see the topic <em>&ldquo;Create a registered application&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
<li style="text-indent: -.25in;">Network Security Manager virtual machine should be deployed in Azure cloud or On-premises.</li>
<li style="text-indent: -.25in;">A vNSP Controller should be created in the Network Security Manager for the Controller to establish communication with the Manager. For more information on creating a Controller in the Manager, see the topic <em>&ldquo;Configure a vNSP Controller in Azure&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
<li style="text-indent: -.25in;">Subscription, Resource Group, Virtual Network, and Subnet should be defined before deploying the Controller.</li>
<li style="text-indent: -.25in;">Make sure to add an inbound rule in the Network Security Manager virtual machine for port 443 for the Controller to successfully register with the Manager. For more information on the ports required for Controller and Manager communication, see the topic &ldquo;<em>Requirements to deploy Network Security Platform in Azure environment&rdquo;</em> in the <em>&ldquo;Virtual IPS Administration Guide</em>&rdquo;.</li>
</ul>
<h2>Deployment</h2>
<p>To deploy the vNSP Controller using the template, perform the following steps:</p>
<ol>
<li style="text-indent: -.25in;">Log in to the machine which has the Azure CLI installed on it.</li>
</ol>
<p>If you are logging in to the Azure CLI for the first time, execute the following command:</p>
<p><span style="font-size: 10.0pt; line-height: 107%; font-family: 'Courier New';">az login</span></p>
<ol start="2">
<li style="text-indent: -.25in;">Execute <span style="font-size: 10.0pt; line-height: 107%; font-family: 'Courier New';">az vm image list --all -p mfe_azure &ndash;-sku mcafee-vnsp-controller</span>.</li>
</ol>
<p>Note the urn generated for the vNSP Controller image.</p>
<ol start="3">
<li style="text-indent: -.25in;">Execute <span style="font-size: 10.0pt; line-height: 107%; font-family: 'Courier New';">az vm image accept-terms --urn &lt;controller_image_urn&gt;</span>.</li>
<li style="text-indent: -.25in;">Go to <a href="https://github.com/mcafee/NSP/tree/master/Azure%20Templates">McAfee Github for vNSP on Azure</a> where the vNSP component templates are available.</li>
<li style="text-indent: -.25in;">In the <strong>Github</strong> page, click <strong>McAfee Controller</strong>.</li>
<li style="text-indent: -.25in;">The <strong>McAfee Controller</strong> template page opens.</li>
<li style="text-indent: -.25in;">Click <strong>Deploy to Azure</strong>.</li>
<li style="text-indent: -.25in;">The <strong>Deploy to Azure</strong> page opens.</li>
<li style="text-indent: -.25in;">Enter the details for the Controller:</li>
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
<p style="margin-bottom: .0001pt; line-height: normal;">Select the Resource Group where the Controller should be deployed.</p>
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
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual machine name for the Controller.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Virtual Machine Size</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual machine size as <strong>Standard_E2s_v3 </strong>.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Admin Username</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter a username for the Controller virtual machine. This should be the same name that was provided in the Network Security Manager.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Admin Password</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter a password for the Controller virtual machine.</p>
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Note:</strong> Only SSH public key authentication type is supported for Controllers.</p>
</td>
</tr>
<tr>
<td style="width: 152.75pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" width="204">
<p style="margin-bottom: .0001pt; line-height: normal;"><strong>Custom Data</strong></p>
</td>
<td style="width: 314.75pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="420">
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the custom data for the Controller as <span style="font-size: 9.0pt; font-family: 'Courier New';">{"Primary NSM IP":"10.x.x.x", "Controller Name":"controller_name", "Controller Shared Key":"passphrase"}</span>. When using an MDR pair, provide the user data as <span style="font-size: 9.0pt; font-family: 'Courier New';">{"Primary NSM IP":"10.x.x.x", "Secondary NSM IP":"10.x.x.x", "Controller Name":"controller_name", "Controller Shared Key":"passphrase"}.</span></p>
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
<p style="margin-bottom: .0001pt; line-height: normal;"><span style="font-size: 9.0pt; font-family: 'Courier New';">Controller Name</span></p>
</td>
<td style="width: 187.45pt; padding: 0in 5.4pt 0in 5.4pt;" width="250">
<p style="margin-bottom: .0001pt; line-height: normal;">Name of the Controller defined in the Manager</p>
</td>
</tr>
<tr>
<td style="width: 116.0pt; padding: 0in 5.4pt 0in 5.4pt;" width="155">
<p style="margin-bottom: .0001pt; line-height: normal;"><span style="font-size: 9.0pt; font-family: 'Courier New';">Controller Shared Key</span></p>
</td>
<td style="width: 187.45pt; padding: 0in 5.4pt 0in 5.4pt;" width="250">
<p style="margin-bottom: .0001pt; line-height: normal;">Shared secret key of the Controller provided in the Manager</p>
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
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the virtual network name where the Controller should be deployed.</p>
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
<p style="margin-bottom: .0001pt; line-height: normal;">Enter the subnet where the Controller should be deployed.</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>Support</h2>
<p>The Controller template is not supported by McAfee through the usual support modes which is McAfee Technical Support. The templates will be updated on a best-effort basis and any troubleshooting in case of template deployment failure will not be supported by McAfee.</p>