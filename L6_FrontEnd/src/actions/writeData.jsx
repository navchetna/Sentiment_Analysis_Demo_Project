"use client";
import { PrismaClient, Prisma } from "@prisma/client";

const prisma = new PrismaClient();

export const writeData = async () => {
  let includePosts = false;
  let user;
  let success = false;

  // Check if posts should be included in the query
  if (includePosts) {
    user = {
      grade: "2",
      name: "Elsa Prisma",
      city: "Bangalore",
    };
  } else {
    user = {
      grade: "1",
      name: "Elsa Prisma",
      city: "Mysore",
    };
  }

  // Pass 'user' object into query
  const createUser = await prisma.user.create({ data: user });
  success = true;
  return success;
};
