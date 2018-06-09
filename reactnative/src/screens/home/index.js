import React, { Component } from "react";
import { ImageBackground, View, StatusBar, Alert, StyleSheet } from "react-native";
import { Container, Button, H3, Text } from "native-base";
import {
  Left,
  Icon, 
  Right,
  Body,
  Header,
  Title,
  Content,
  Form,
  Label,
  Input,
  Item
} from "native-base";
import styles from "./styles";

const launchscreenBg = require("../../../assets/launchscreen-bg.png");
const launchscreenLogo = require("../../../assets/logo-kitchen-sink.png");

class Home extends Component {

  render() {
    return (


      <Container style={styles.container}>
        <StatusBar barStyle="light-content" />
        <ImageBackground source={launchscreenBg} style={styles.imageContainer}>




          <View style={styles.logoContainer}>
            <ImageBackground source={launchscreenLogo} style={styles.logo} />
          </View>



          <View
            style={{
              alignItems: "center",
              marginBottom: 50,
              backgroundColor: "transparent"
            }}
          >
          </View>


          <Content>
          <Form>
            <Item floatingLabel>
              <Label>Driver License ID</Label>
              <Input />
            </Item>
            <Item floatingLabel last>
              <Label >Password</Label>
              <Input secureTextEntry />
            </Item>
          </Form>
        </Content>
          




          <View style={{ marginBottom: 120 }}>
            <Button
              style={{ backgroundColor: "#014225", alignSelf: "center", marginTop: 10, padding: 10 }}
                onPress={() => this.props.navigation.navigate("DrawerOpen")}
            >
              <Text>Login</Text>
            </Button>

            <Button
              style={{ backgroundColor: "#014225", alignSelf: "center", marginTop: 10, padding: 10 }}
            >
            <Text>Register</Text>
            </Button>
            
          </View>
        </ImageBackground>
      </Container>
    );
  }
}

export default Home;
