import {
  DesktopOutlined,
  FileOutlined,
  PieChartOutlined,
  TeamOutlined,
  UserOutlined,
} from "@ant-design/icons";

function getItem(label, key, icon, children) {
  return {
    key,
    icon,
    children,
    label,
  };
}

const sidebarItems = [
  getItem("Profile ", "1", <PieChartOutlined />),
  getItem("Presentation", "2", <DesktopOutlined />),
  getItem("Users", "sub1", <UserOutlined />, [
    getItem("Tom", "3"),
    getItem("Bill", "4"),
    getItem("Alex", "5"),
  ]),
  getItem("Teams", "sub2", <TeamOutlined />, [
    getItem("Team 1", "6"),
    getItem("Team 2", "8"),
  ]),
  getItem("Files", "9", <FileOutlined />, [
    getItem("File 1", "10"),
    getItem("File 2", "11"),
  ]),
];

export default { sidebarItems };
