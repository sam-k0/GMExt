## fuck you python

def readexfile(path): ## reads all lines from file and returns string
    with open("data.txt") as myfile:
        data = "".join(line.rstrip() for line in myfile)
        return data


EXTENSIONSTRING = """<extension>
  <name>TextEx</name>
  <version>1.0.0</version>
  <packageID></packageID>
  <ProductID>ACBD3CFF4E539AD869A0E8E3B4B022DD</ProductID>
  <date>06/03/22</date>
  <license>Free to use, also for commercial games.</license>
  <description></description>
  <helpfile></helpfile>
  <installdir></installdir>
  <classname></classname>
  <androidclassname></androidclassname>
  <sourcedir></sourcedir>
  <androidsourcedir></androidsourcedir>
  <macsourcedir></macsourcedir>
  <maclinkerflags></maclinkerflags>
  <maccompilerflags></maccompilerflags>
  <androidinject></androidinject>
  <androidmanifestinject></androidmanifestinject>
  <iosplistinject></iosplistinject>
  <androidactivityinject></androidactivityinject>
  <gradleinject></gradleinject>
  <iosSystemFrameworks/>
  <iosThirdPartyFrameworks/>
  <ConfigOptions>
    <Config name="Default">
      <CopyToMask>64</CopyToMask>
    </Config>
  </ConfigOptions>
  <androidPermissions/>
  <IncludedResources/>
  <files>
    <file>
      <filename>Max WinAPI 2.dll</filename>
      <origname>extensions\Max WinAPI 2.dll</origname>
      <init></init>
      <final></final>
      <kind>1</kind>
      <uncompress>0</uncompress>
      <ConfigOptions>
        <Config name="Default">
          <CopyToMask>9223372036854775807</CopyToMask>
        </Config>
      </ConfigOptions>
      <ProxyFiles/>
      <functions>
        <function>
          <name>hobbl_com_cb_create</name>
          <externalName>hobbl_com_cb_create</externalName>
          <kind>11</kind>
          <help></help>
          <returnType>2</returnType>
          <argCount>7</argCount>
          <args>
            <arg>2</arg>
            <arg>2</arg>
            <arg>2</arg>
            <arg>2</arg>
            <arg>2</arg>
            <arg>2</arg>
            <arg>2</arg>
          </args>
        </function>
        <function>
          <name>amogus_function2</name>
          <externalName>amogus_function2</externalName>
          <kind>11</kind>
          <help></help>
          <returnType>1</returnType>
          <argCount>2</argCount>
          <args>
            <arg>1</arg>
            <arg>2</arg>
          </args>
        </function>
      </functions>
      <constants>
        <constant>
          <name>GW_CHILD</name>
          <value>5</value>
          <hidden>0</hidden>
        </constant>
        <constant>
          <name>macro2</name>
          <value>69</value>
          <hidden>0</hidden>
        </constant>
      </constants>
    </file>
  </files>
</extension>
"""