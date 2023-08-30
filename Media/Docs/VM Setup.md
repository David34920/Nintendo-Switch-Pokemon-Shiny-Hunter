<h1 align="center">
    <br><img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/Virtual%20Box%20and%20Linux.png" width="50%"></br>
</h1>

<h2>
    <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/SVG/Virtual%20Box.svg" width="30px" align="top"/>
    Download Virtual Box (VBox) and Linux ISO
</h2>

- Go to the [Virtual Box Official Webpage](https://www.virtualbox.org/wiki/Downloads). Download and install the correct *VirtualBox Platform Package* for your operating system. 
- Feel free to use the OS you feel more comfortable with; I'm using **XUbuntu**, but other Linux distributions will work as well. Go to [XUbuntu Webpage](https://xubuntu.org/download/). Select your nearest location to get the mirror and download the *xubuntu-xx.xx.x-desktop-amd64.iso*, where *xx.xx.x* is the version of the ISO (I'm currently using the version *22.04.3*). The file is about 3GB; it's the operating system of the Virtual Machine.

<h2>
    <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/SVG/Gear.svg" width="25px" align="top"/>
    Setup the Virtual Machine
</h2>

### Create the Virtual Machine

<ul>
    <li>
        <p>Open <strong>Oracle VM VirtualBox</strong> and click the <code>Add New</code> button.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%201.png" width="50%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>Write a name for the Virtual Machine and select the ISO. Click the <code>Next</code> button.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%202.png" width="70%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>Create your username and password. If the <i>Additional Options</i> box raises a warning, replace spaces " " by "-". Click the <code>Next</code> button.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%203.png" width="70%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>The following step depends on the specifications of your computer. You can assign more or less RAM and Cores depending on how powerful your computer is. 4GB of RAM and 2 Cores are enough. Click the <code>Next</code> button.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%204.png" width="70%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>Select the <i>Create Virtual Disc Now</i> option and assign it about 20GB of memory. Click the <code>Next</code> button and then, <code>Finish</code>.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%205.png" width="70%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>The Virtual Machine will automatically start. Wait until it completes the installation. From now on, you can make your mouse exit the Virtual Machine by pressing <i>Right Ctrl</i> key.</p>
    </li>
</ul>

### Configure the Virtual Machine

<ul>
    <li>
        <p>Once the installation has finished, click the <i>Windows</i> key and type <code>keyboard</code>. Click on the settings button, select your keyboard layout and remove the default one.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2010.png" width="70%" style="border-radius: 5px;">
            <p></p>
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2011.png" width="50%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>Click Windows key and type <code>language</code>. Click on the settings button and select your Time and Format. <strong>IMPORTANT:</strong> Even if your language is the default one, <i>English (United States)</i>, change it to whatever, click the green <code>Restart</code> button, then change it back and click the green <code>Restart</code> button again. It's important not to skip this step; otherwise, you may have problems trying to open terminals.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%206.png" width="70%" style="border-radius: 5px;">
            <p></p>
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2012.png" width="70%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>You may have noticed that when opening VBox in fullscreen mode, it does not scale correctly, leaving gray spaces at the borders.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%207.png" width="70%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>To solve this issue, <i>Right Click</i> on the Desktop and select <i>Open in Terminal</i>. Run the following commands one by one:</p>
<pre><code>su 
nano /etc/sudoers</code></pre>
        <p>Add the following line changing <i>dinones</i> by your username:</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2013.png" width="70%" style="border-radius: 5px;">
        </h6>
        <p>Save the file pressing <i>Ctrl + S</i> and then <i>Ctrl + X</i>. Once back in the terminal, run:</p>
<pre><code>exit
sudo apt update</code></pre>
    </li>
    <li>
        <p>Now, in the VBox top menu, click on <i>Devices</i> > <i>Insert Guest Additions CD Image</i>.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%208.png" width="60%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>A disc icon should appear in the task bar. Open it, <i>Right Click</i> inside the folder, and select <i>Open in Terminal</i>. Run the following command:</p>
        <pre><code>./autorun.sh</code></pre>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%209.png" width="70%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p>Wait until the installation is finished and restart the Virtual Machine. Now, you should be able to use the fullscreen mode without seeing the gray borders. If not, go to the VBox top menu, click on <i>View</i> > <i>Virtual Screen 1</i> and select your screen resolution, which will probably be 1920x1080.</p>
    </li>
</ul>

### [Optional] Extra Configurations for the Virtual Machine 

The following configurations are completely optional, but highly recommended for a more friendly experience:

<ul>
    <li>
        <p><strong>Remove Terminal Bell Sound</strong></p>
        Open a terminal. Go to <i>Preferences</i>, select your profile, probably called <i>"Unnamed"</i> and uncheck the <i>Terminal Bell</i>.
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2015.png" width="70%" style="border-radius: 5px;">
        </h6>
    </li>
    <li>
        <p><strong>Run <i>sudo</i> Commands without Entering Password</strong></p>
        <p>Open a terminal and run the following command:</p>
        <pre><code>sudo visudo</code></pre>
        <p>Add the following line changing <i>dinones</i> by your username:</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2016.png" width="70%" style="border-radius: 5px;">
        </h6>
        <p>Save the file pressing <i>Ctrl + S</i> and then <i>Ctrl + X</i>.</p>
    </li>
    <li>
        <p><strong>Enable Shared Clipboard</strong></p>
        <p>Power off the VM. Open <strong>Oracle VM VirtualBox</strong>, select your VM and click the <code>Configuration</code> button.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2017.png" width="50%" style="border-radius: 5px;">
        </h6>
        <p>Go to <i>General</i> > <i>Advanced</i> and change both options to "<i>Bidirectional</i>".</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2018.png" width="70%" style="border-radius: 5px;">
        </h6>
        <p>You should now be able to drag and drop files and also copy and paste text from/to the virtual machine to/from your personal computer.</p>
    </li>
    <li>
        <p><strong>Create a Shared Folder between your Computer and the VM</strong></p>
        <p>Power off the VM. Open <strong>Oracle VM VirtualBox</strong>, select your VM and click the <code>Configuration</code> button. Go to <i>Shared Folders</i> and click the <code>Add New Shared Folder</code> button. In the window that pops up, select your shared folder and check the <i>Automount</i> option.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2019.png" width="70%" style="border-radius: 5px;">
        </h6>
        <p>Turn on the VM, open a terminal and run the following command:</p>
        <pre><code>sudo adduser $USER vboxsf</code></pre>
        <p>Restart the VM. Open the file manager. There should be an extra folder whose content is shared with your personal computer.</p>
        <h6 align="center">
            <img src="https://raw.githubusercontent.com/Dinones/Repository-Images/master/VBox%20Instructions/VBox%2020.png" width="70%" style="border-radius: 5px;">
        </h6>
    </li>
</ul>