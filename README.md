### 지혜 보따리 실행 코드

import sys  
srcPath = "jhScriptUI.py 파일이 들어있는 경로"  
if not srcPath in sys.path:  
&nbsp;&nbsp;&nbsp;&nbsp;sys.path.append(srcPath)  
import jhScriptUI  
reload(jhScriptUI)  
jhScriptUI.main()

### Notice
윈도우 & 리눅스 모두 정상 작동을 확인했습니다만  
kk_controllers 실행 시 아이콘 경로를 제대로 인식하지 못해서 아이콘이 안나옵니다. :(  
사실 덱스터에서 kk_controllers 툴을 사용할 일이 있을까 싶긴 합니다만  
어쩔 수 없이 필요한 경우에는 다음과 같이 하시면 아이콘이 표시 됩니다.  


kk_controllersMD.mel 파일을 메모장으로 열어서  
위 스샷의 녹색 부분에 아이콘 폴더 경로를 바꿔 넣어주시면 됩니다.  
예를 들어 /downloads/jhScriptBase/ 경로에 스크립트가 들어있다고 한다면  
string $icon_path= $inhouseMayaPath+"/kk_icons/";라고 되어있는 것을  
string $icon_path= "/downloads/jhScriptBase/scripts/kk_icons/"; 라고 경로를 바꿔주시면 됩니다.  
경로 마지막에 / (슬래시) 붙이는 것을 잊지 마시길 바랍니다.

- Anim School Picker (애님 픽커 다운로드 사이트)  
www.animschool.com/pickerInfo.aspx

- Hold Out (홀드 아웃 다운로드 사이트)  
www.highend3d.com/maya/plugin/holdout-shader-for-maya
