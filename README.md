# New Hire Script

## Requirements
You'll need Microsoft's Active Directory module installed on the machine this will be running on. This requires Microsoft's RSAT package. A nice script to do all of this on Windows 10 can be found here: <https://blogs.technet.microsoft.com/ashleymcglone/2016/02/26/install-the-active-directory-powershell-module-on-windows-10/>

If your Exchange version is 2007 or below, you can use the Exchange PS Snapin. You can get this by installing Exchange Management Tools 2007 (32-bit version found here: <https://www.microsoft.com/en-us/download/details.aspx?id=11876>)
If your Exchange is 2010 or greater, you'll need to do a little extra work to set up Remote Powershell to the Exchange server. A TechNet article on that can be found here: <https://blogs.technet.microsoft.com/rmilne/2015/01/28/directly-loading-exchange-2010-or-2013-snapin-is-not-supported/>
