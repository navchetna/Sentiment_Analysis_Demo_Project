import React, { useState } from "react";
import { Breadcrumb, Layout, Menu, theme } from "antd";
const { Header, Content, Footer, Sider } = Layout;
import SidebarItemsConfig from "../config/SidebarItemsConfig";

const Sidebar = ({ sidebarItems }) => {
  const [collapsed, setCollapsed] = useState(false);
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();
  return (
    <>
      <Layout
        style={{
          maxWidth: "fit-content",
        }}
      >
        <Layout
          style={{
            minHeight: "100vh",
          }}
        >
          <Sider
            collapsible
            collapsed={collapsed}
            onCollapse={(value) => setCollapsed(value)}
          >
            <div className="demo-logo-vertical mt-24" />
            <Menu
              theme="dark"
              defaultSelectedKeys={["1"]}
              mode="inline"
              items={SidebarItemsConfig.sidebarItems}
            />
          </Sider>
        </Layout>
      </Layout>
    </>
  );
};
export default Sidebar;
